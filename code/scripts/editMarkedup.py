#!/usr/bin/env python
"""
Edit markedup categories more intelligently, by comparing novel categories
with existing ones
"""
import re, sys
import CCG
from os.path import join as pjoin


def readMarkedup(markedupLoc, extend = True):
    """
    Map the bare categories to their mark up
    """
    cats = {}
    currEntry = []
    try:
        muFile = open(markedupLoc)
    except IOError:
        return {}
    for line in muFile:
        line = line.strip()
        if line.startswith('#'):
            continue
        if line.startswith('='):
            continue
        if not line:
            if currEntry:
                bare = CCG.Category(currEntry[0])
                annot = currEntry[1]
                annot = annot.strip()[2:]
                # Remove [X] feature place holders -- we'll add them back when we output
                # This is easier than fiddling the (already horrible) highlight matching
                # regex further
                annot = annot.replace('[X]', '')
                annot = annot[:-3]
                if bare.isComplex():
                    # Refer to unbracketed version, for matching later
                    cats[bare] = annot[1:-1]
                    LOG.write("Caching: %s %s\n" % (bare, annot[1:-1]))
                else:
                    cats[bare] = str(bare)
               # annot = annot[1:-1]
                if extend and bare.isComplex():
                    annot = _annotResult(annot)
                    bare = bare.result
                    # Add results as well as whole category
                    while bare.isComplex():
                        # Remove head index
                        annot = annot[:-3]
                        # Strip outer brackets
                        cats[bare] = annot[1:-1]
                        LOG.write("Caching from res: %s %s\n" % (bare, annot[1:-1]))
                        annot = _annotResult(annot)
                        bare = bare.result
            currEntry = []
        else:
            currEntry.append(line)
    return cats



def _annotResult(annot):
    """
    Strip off the last arg of the annotated category, without using
    the CCG.Category class (as we need the annotation)
    """
    depth = 0
    for i, char in enumerate(annot):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif depth == 1 and char in ['/', '\\', '^']:
            # We must start at 1, as we don't want the first bracket -- as that matches
            # the bracket at the end
            annot = annot[1:i]
            # remove arg def
            if annot.endswith('>'):
                 annot = annot[:-3]
            break
    return annot




# Need new style class to support property
class Controller(object):
    """
    Control the printing to Header, Category and Prompt and the logic flow
    of category annotation
    """
    def __init__(self, stdscr):
        self._stdscr = stdscr
        y, x = stdscr.getmaxyx()
        self.windowWidth = x
        self.header = Header(self)
        self._headerWindow = stdscr.subwin(0, 0)
        self.category = Category(self)
        self._categoryWindow = stdscr.subwin(0, 0)
        self.prompt = Prompt(self)
        self._promptWindow = stdscr.subwin(0, 0)
        self._textWindow = stdscr.subwin(0, 0)
        self._textBox = curses.textpad.Textbox(self._textWindow)


    
    def findMatch(self, category):
        muCats = self.muCats
        result = category
        resultSet = {result: True}
        while result.isComplex():
            resultSet[result] = True
            if result.morph:
                morphless = CCG.Category(result.morphLess())
                resultSet[morphless] = True
            result = result.result
        catObj = self.category
        prompt = self.prompt
        queue = self._getCatQueue(category)
        queue.reverse()
        for i, cat in enumerate(queue):
            LOG.write("Q: %s (%d)\n" % (cat, i))
        candidates = []
        seen = {}
        for i, cat in enumerate(queue):
            if cat in resultSet and cat not in seen:
                candidates.append((len(str(cat)), cat, i))
                seen[cat] = True
        candidates.sort()
        candidates.reverse()
        # Hack for no suggested matches
        candidates = []
        for length, cat, i in candidates:
            annot = muCats.get(cat, '')
            if annot:
                catObj.highlight(cat)
                reply = prompt.suggestMatch(cat, annot)
                if reply == 'y':
                    # Trim queue of cats subsumed by the match
                    queue = queue[i:]
                    LOG.write("Trimming at: %d (%s)" % (i, cat))
                    catObj.replaceAnnot(annot)
                    break
        return queue


    def doQueue(self, queue):
        """
        Proceed through the queue of categories to be annotated,
        expanding complex categories so that their pieces jump to the front
        of the queue
        """
        category = self.category
        while queue:
            cat = queue.pop(0)
            annot = self.getAnnot(cat)
            category.addAnnot(annot)

    def checkAdjunct(self, category):
        """
        If category says it's an adjunct, ask the user whether to handle it as one
        """
        if category.isAdjunct():
            adjAnswer = self.prompt.askAdjunct()
            if adjAnswer == 'y':
                return True
        return False
    

    def _getCatQueue(self, cat):
        queue = []
        while cat.isComplex() or cat.morph:
            # Do argument first, so add cat first before reversal
            if cat.morph:
                morph = cat.morph
                queue.append(morph)
                if morph.isComplex():
                    queue.extend(self._getCatQueue(morph.argument))
                    queue.extend(self._getCatQueue(morph.result))
                queue.append(CCG.Category(cat.morphLess()))
                if not cat.isComplex():
                    break
            else:
                queue.append(cat)
            argument = cat.argument
            queue.append(argument)
            if cat.argument.isComplex():
                queue.extend(self._getCatQueue(argument.argument))
                queue.extend(self._getCatQueue(argument.result))
            cat = cat.result
        else:
            queue.append(cat)
        return queue


    def getAnnot(self, arg):
        """
        Add annotation for a constituent
        """
        arg = arg.strAsPiece()
        self.category.highlight(arg)
        headIdx = self.prompt.getHeadIdx()
        if self.category.argHighlight:
            isArg = self.prompt.askArg()
            if isArg == 'y':
                argIdx = "<%d>" % self.category.argSuggest
            else:
                argIdx = ''
        else:
            argIdx = ''
        annot = "%s%s" % (headIdx, argIdx)
        return annot
        
    def doCat(self, cat, comments, progress):
        self.clear()
        self.header.newCat(cat, comments, progress)
        self.category.newCat(cat)
        self.prompt.newCat(cat)
        self._textWindow.erase()
        queue = self.findMatch(cat)
        # Don't need to ask for last head index; must be X
        if queue:
            queue.pop()
        self.doQueue(queue)
        LOG.write("Annot: %s\n" % repr(self.annot))
        self.annot = self.annot + '{_}'
        self.annot = self.completionPrompt()
        self.updateMU()

    
    def updateMU(self):
        bare = self.category.category
        annot = self.category.annot
        muEntry = self.formatEntry(bare, annot)
        open(outputMU, 'a').write(muEntry)
        annot = annot[:-3]
        while bare.isComplex():
            annot = annot[:-3]
            muCats[bare] = annot[1:-1]
            bare = bare.result
            annot = _annotResult(annot)
            

    _addSFeatRE = re.compile(r'S(?!\[)')
    def formatEntry(self, bare, annot):
        argNum = self.category.argSuggest - 1
        args = []
        for i in xrange(argNum):
            args.append("  %d ignore" % (i + 1))
        comments = self.header.comments
        bare = bare
        # Add the [X] feature place holder to S
        annot = Controller._addSFeatRE.sub('S[X]', annot)
        # Template looks like:
        # [comments]
        # bare
        #   num annot
        #   1 ignore
        #   ...
        template = "%s\n%s\n  %d %s\n%s\n\n"
        formatted = template % ('\n'.join(comments), bare, argNum, annot, '\n'.join(args))
        return formatted

    def display(self):
        """
        Arrange the windows and display
        """
        headerSize = self.header.size
        categoryPlace = headerSize
        if headerSize > 0:
            categoryPlace += 1
        categorySize = self.category.size
        promptPlace = categoryPlace + categorySize
        if categorySize > 0:
            promptPlace += 1
        promptSize = self.prompt.size
        textPlace = promptPlace + promptSize
        if promptSize > 0:
            textPlace += 1
        # Clear the windows
        self._headerWindow.erase()
        self._categoryWindow.erase()
        self._promptWindow.erase()
        # Move the windows
        self._categoryWindow.move(categoryPlace, 0)
        self._promptWindow.move(promptPlace, 0)
        self._textWindow.move(textPlace, 0)
        # Update the windows
        def addStr(window, theBuffer):
            for message, mode in theBuffer:
                if mode:
                    window.addstr(message, mode)
                else:
                    window.addstr(message)
        addStr(self._headerWindow, self.header.buffer)
        addStr(self._categoryWindow, self.category.buffer)
        addStr(self._promptWindow, self.prompt.buffer)
        # Draw the windows
        self._headerWindow.refresh()
        self._categoryWindow.refresh()
        self._promptWindow.refresh()
        self._textWindow.refresh()

    def doPrompt(self, message, singleChar = False):
        """
        Display a message and get some input back
        """
        prompt = self.prompt
        window = self._promptWindow
        prompt.clear()
        prompt.add(message + '\n')
        self.display()
        if singleChar:
            answer = chr(window.getch())
            if answer == 'q':
                confirm = self.doPrompt("Type 'quit' to exit.")
                if confirm == 'quit':
                    sys.exit(1)
        else:
            chars = []
            while True:
                char = chr(window.getch())
                prompt.add(char)
                self.display()
                if char == '\n':
                    answer = ''.join(chars)
                    if answer == 'quit':
                        sys.exit(1)
                    break
                chars.append(char)
        prompt.clear()
        return answer

    # Make this a class attribute so that we can use it to extract the answer
    compPromptText = "Edit category. Replace a head index like {Y} with {Y! to add an arg index. ctrl+g to end"
    def completionPrompt(self, seed = None):
        """
        Ask the user to accept or change the annotation
        """
        if not seed:
            seed = self.annot
            self.prompt.addLine(Controller.compPromptText)
            self.display()
            self._textWindow.addstr(self.category.annot)
            self._textWindow.refresh()
            self._textBox.stripSpace = 1
        category = self.textBox(seed)
        return category


    def textBox(self, seed = ''):
        """
        Use text window to get answer
        """
        screen = self._textBox.edit()
        answer = self._trimAnswer(screen)
        answer = self._fixArgs(answer)
        return answer
       # accept = self.doPrompt("c to continue editing, y to accept, b to edit original\n%s" % answer, True)
       # if accept == 'c':
       #     self.prompt.clear()
       #     self.completionPrompt(answer)
       # elif accept == 'b':
       #     self.prompt.clear()
       #     self.completionPrompt(self.annot)
       # return answer

    _answerFindRE = re.compile(r'(?<=%s).+' % re.escape(compPromptText.replace('\n', '')))
    def _trimAnswer(self, screen):
        LOG.write("Textbox screen:\n%s" % screen)
        LOG.write("Pattern: %s" % Controller._answerFindRE.pattern)
        # When the line wraps, newlines can be inserted anywhere. So take them out.
        screen = screen.replace('\n', '')
        answer = Controller._answerFindRE.search(screen).group()
        LOG.write("Textbox answer:\n%s\n" % answer)
        return answer


    _argFixRE = re.compile(r'!|\d')
    def _fixArgs(self, answer):
        args = Controller._argFixRE.findall(answer)
        lastArg = 0
        replaces = []
        increment = 0
        for arg in args:
            if arg == '!':
                lastArg += 1
                # If we insert this as '<2>', when we replace 2 with 3 later,
                # it'll get replaced instead. So make it look different and
                # fix it later
                replaces.append((arg, '}*%d!' % lastArg))
                increment += 1
            elif increment:
                newArg = int(arg) + increment
                replaces.append(('<%s>' % arg, '<%d>' % newArg))
                lastArg = newArg
            else:
                lastArg = int(arg)
        for old, new in replaces:
            answer = answer.replace(old, new, 1)
        answer = answer.replace('*', '<')
        answer = answer.replace('!', '>')
        return answer
        


    def clear(self):
        self.header.clear()
        self.category.clear()
        self.prompt.clear()
        self._textWindow.erase()

    def wait(self):
        self._stdscr.getch()

    def addError(self, error):
        """
        Add error to prompt buffer
        """
        self.prompt.add(error)
        LOG.write("Err msg: %s" % error)

    def doError(self):
        self.display()
        self.wait()
        raise StandardError

    def preamble(self):
        self.prompt.preamble()

    def _getAnnot(self):
        return self.category.annot

    def _setAnnot(self, newAnnot):
        assert type(newAnnot) == str
        self.category.annot = newAnnot

    annot = property(_getAnnot, _setAnnot)





class SubWindow(object):
    """
    A curses sub window
    """
    def __init__(self, controller):
        self._controller = controller
        self.windowWidth = controller.windowWidth
        self.buffer = []

    def _getSize(self):
        """
        Count the number of lines needed to display the buffer. This includes
        how often a line will need to wrap
        """
        lines = 0
        lineLen = 0
        for message, mode in self.buffer:
            for char in message:
                if char == '\n':
                    lines += 1
                    lineLen = 0
                else:
                    lineLen += 1
                if lineLen == self.windowWidth:
                    lines += 1
                    lineLen = 0
        if lineLen:
            lines += 1
        return lines

    size = property(_getSize)
            
    
    def add(self, message, mode = None):
        """
        Add to the window buffer
        """
        self.buffer.append((str(message), mode))


    def addLine(self, message, mode = None):
        self.add(str(message) + '\n', mode)

    def clear(self):
        """
        Clear the window
        """
        self.buffer = []


    def display(self):
        """
        Display the buffered messages
        """
        self._controller.display()

    def prompt(self, message, singleChar = False):
        return self._controller.doPrompt(message, singleChar)

    def wait(self):
        self._controller.wait()

    def addError(self, message):
        self._controller.addError(message)

    def doError(self):
        self._controller.doError()
        
    def _cantSet(self):
        raise AttributeError
    






    


class Header(SubWindow):
    """
    The header displayed while annotating a category
    """ 
    def newCat(self, cat, comments, progress):
        self.clear()
        cat = str(cat)
        self.addLine(cat)
        self.addLine(progress)
        for comment in comments:
            # Highlight category
            catStart = comment.find(cat)
            if catStart == -1:
                self.addLine(comment)
            else:
                begin = comment[:catStart]
                catEnd = catStart + len(cat)
                end = comment[catEnd:]
                self.add(begin)
                self.add(cat, curses.A_STANDOUT)
                self.addLine(end)
        self.comments = comments
        self.display()

class Category(SubWindow):
    """
    The annotation progress on a category, with the section under review in bold
    """
    height = 1
    def newCat(self, category):
        self.category = category
        self.annot = category.strAsPiece()
        self.add(self.annot)
        results = {}
        while category.isComplex():
            # finding the number of brackets will be hard later, so remove
            # all of them for simple matching
            result = str(category.result).replace('(', '')
            result = result.replace(')', '')
            results[result] = True
            category = category.result
        self.resultSet = results
        self.display()

    
    def addAnnot(self, annotated):
        """
        Add annotation after the highlighted category
        """
        before = self.annot[:self.end]
        after = self.annot[self.end:]
        self.annot = before + annotated + after


    def replaceAnnot(self, annotated):
        """
        Replace the highlighted category with the annotation
        (used for findMatch)
        """
        before = self.annot[:self.start]
        after = self.annot[self.end:]
        self.annot = before + annotated + after

    def highlight(self, category):
        """
        Highlight a new section of the category
        """
        catRE = self._genCatExp(str(category))
        matchObj = catRE.search(self.annot)
        if matchObj:
            self.start = matchObj.start()
            self.end = matchObj.end()
        else:
            self.addError("Error coming from non-match\n")
            self.addError(str(category) + '\n')
            self.addError(self.annot + '\n')
            self.addError(catRE.pattern + '\n')
            self.doError()
        self._updateDisplay()
        

    expGenRE = re.compile('(?:(?:[A-Z]+)|(?:\)))(?:\[\w+])?(?=\W)')
    def _genCatExp(self, catStr):
        """
        Truly horrible solution: decorate category with a regular expression to
        make it match on the annotated category. This involves using another regular
        expression, expGenRE, to find the places where annotation might occur
        """
        # Feeding this to re.sub is just like using \1
        def replacer(matchObj):
            # Don't put in the real regexp just yet -- we need to escape the original
            return matchObj.group() + 'PATTERN'
        ignoreAnnot = r'(?:\{\w\})?(?:<\d>)?\)*?'
        # Do the replacement with PATTERN holding place for the ignoreAnnot string
        catExp = Category.expGenRE.sub(replacer, catStr)
        # Escape the brackets etc in the category, so re doesn't complain
        catExp = re.escape(catExp)
        # Insert the expression to ignore the annotation
        catExp = catExp.replace(r'PATTERN', ignoreAnnot)
        # Add a look ahead to avoid matching already annotated examples
        catExp += r'(?!\{\w\})'
        # Add another look ahead to avoid matching NP with N and S[ with S
        catExp += r'(?![\w\[])'
        return re.compile(catExp)

    def _updateDisplay(self):
        self.clear()
        annot = self.annot
        start = self.start
        end = self.end
        begin = annot[:start]
        cat = annot[start:end]
        end = annot[end:]
        self.add(begin)
        self.add(cat, curses.A_STANDOUT)
        self.add(end)
#        self.add(''.join(annot))
        self.display()

    argRE = re.compile(r'(?<=<)\d(?=>)')
    def _getArgSuggest(self):
        argNums = Category.argRE.findall(self.annot)
        if not argNums:
            return 1
        argSuggest = int(max(argNums)) + 1
        return argSuggest

    annotStripRE = re.compile(r'\{\w\*?\}|<\d>|[\(\)]')
    def _getArgHighlight(self):
        """
        Determine whether the highlighted category is an argument of the main
        category, by checking whether the unhighlighted section matches one
        of the category's results
        """
        # Start at 1 to get rid of outer brackets
        annotResult = self.annot[:self.start - 1]
        result = Category.annotStripRE.sub('', annotResult)
        return bool(result in self.resultSet)
        
    argHighlight = property(_getArgHighlight)
    argSuggest = property(_getArgSuggest)



class Prompt(SubWindow):
    """
    A prompt window telling the user what's going on

    Each prompt type is implemented as a method
    """
    def preamble(self):
        self.add("Annotating categories.\n")
        self.add("Type quit at any prompt to exit.\n")
        self.add("Completed annotations auto-saved to output.\n")
        self.add("Head indices are case insensitive. ")
        self.add("X is mapped to the category head, _, throughout.\n")
        self.add("Entries in the missing categories file should be new line delimited. ")
        self.add("Comment lines (beginning with #) will be preserved in the output markedup file.")
        self.display()
        self.wait()
        self.clear()
    
    def newCat(self, category):
        self.clear()

    headRE = re.compile('(?<={)[A-Z](?=})')
    def _getHeads(self):
        headList = Prompt.headRE.findall(self.annot)
        headList.append('X')
        if not headList:
           # print annot
            raise StandardError
        headSet = {}
        for h in headList:
            headSet[h] = True
        return headSet

    def _getHeadList(self):
        heads = self.heads.keys()
        heads.sort()
        return heads


    heads = property(_getHeads, SubWindow._cantSet)
    headList = property(_getHeadList, SubWindow._cantSet)
        
        
    def suggestMatch(self, cat, match):
        """
        Ask the user whether they want to accept the match annotation
        """
        
        prompt = "%s\nAccept match?" % (match)
        answer = self.prompt(prompt, True)
        return answer

    def askArg(self):
        """
        Ask the user whether the highlighted section needs an argument index
        """
        prompt = "Add dependency? y/n"
        answer = self.prompt(prompt, True)
        return answer

    def getHeadIdx(self):
        """
        Prompt the user to supply the head idx for the current constituent
        """
        headSuggest = self._getHeadSuggest()
        prompt = "Enter coindexed variable from %s, or enter for new head" % ', '.join(self.headList)
        answer = self.prompt(prompt, True)
        if answer == '\n':
            self.display()
            answer = headSuggest
        else:
            answer = answer.upper()
        if answer == 'X':
            answer = '_'
        return '{%s}' % answer

    def _getHeadSuggest(self):
        if self.headList[-1] == 'X':
            return 'Y'
        elif self.headList[-1] == 'Y':
            return 'Z'
        else:
            head = chr(ord(self.headList[0]) - 1)
            self.headList.append(head)
            self.heads[head] = True
            return head
        
    
    def inputMULocation(self):
        """
        Prompt the user to provide the input markedup location
        """
        location = self.prompt("Enter location of seed markedup file")
        return location

    def outputMULocation(self):
        """
        Prompt the user to provide the output markedup location
        """
        location = self.prompt("Enter location of output markedup file")
        return location

    def missingCatsLocation(self):
        """
        Prompt the user to provide the missing cats location
        """
        location = self.prompt("Enter location of missing categories file")

    
    def checkAdjunct(self):
        promptText = "Handle this category as an adjunct (i.e. copy annotation to both parts)? y/n"
        return self.prompt(promptText)


    def _getAnnot(self):
        return self._controller.annot

    
    
    annot = property(_getAnnot, SubWindow._cantSet)








def main(stdscr):
    global inputMU, outputMU, catsLoc, muCats
    controller = Controller(stdscr)
   # inputMU = PROMPT.inputMULocation()
   # outputMU = PROMPT.outputMULocation()
   # catsLoc = PROMPT.missingCatsLocation()
#    inputMU = "/home/mhonn/Data/markedupFiles/markedup_v4.2"
#    catsLoc = "/home/mhonn/code/mhonn/CCG/morphtr_missing.txt"
#    outputMU = "/home/mhonn/code/mhonn/CCG/morphtr_additions.txt"
    muCats = readMarkedup(inputMU)
    muCats.update(readMarkedup(outputMU))
    controller.muCats = muCats
    # Read the output so that we can ignore categories done in a previous session
    exclude = readMarkedup(outputMU, False)
    comments = []
    catLines = open(catsLoc).read().split('\n')
    cats = []
    comments = []
    for lineNum, line in enumerate(catLines):
        if line.startswith('#'):
            comments.append(line)
            continue
        if not line.strip():
            continue
        if line in exclude:
            comments = []
            continue
        # Pre-build this way so we can display both line number and number of categories
        cats.append((line, comments, lineNum))
        comments = []
    numCats = len(cats)
    controller.preamble()
    for i, pieces in enumerate(cats):
        cat, comments, lineNum = pieces
        LOG.write("Cat: %s\n" % cat)
        try:
            cat = CCG.Category(cat)
        except:
            raise StandardError, "Error loading category on line %d of categories file:\n%s" % (lineNum, cat)
            sys.exit(1)
        progress = '%d/%d' % (i + 1, numCats)
        controller.doCat(cat, comments, progress)



def debug(stdscr):
    controller = Controller(stdscr)
    inputMU = "/home/mhonn/Data/markedupFiles/markedup_v1"
    inputMU = "/home/mhonn/Data/markedupFiles/markedup_v1"
    catsLoc = "/home/mhonn/code/mhonn/CCG/missingCats.txt"
    outputMU = "/home/mhonn/code/mhonn/CCG/muEditOutput.txt"
    muCats = readMarkedup(inputMU)
    controller.muCats = muCats
   # HEADER.preamble()
   # inputMU = PROMPT.inputMULocation()
   # outputMU = PROMPT.outputMULocation()
   # catsLoc = PROMPT.missingCatsLocation()
    cat = CCG.Category('((NA/NB)/(NC/ND))/((NE/NF)/(NG/NH))')
    muCats[cat.result] = True
    muCats[cat.result.result] = True
    controller.category.newCat(cat)
    controller.findMatch(cat)
   # queue = controller._getCatQueue(cat)
   # for cat in queue:
   #     controller.prompt.addLine(cat)
   # controller.display()
   # controller.wait()
    """
    inputMU = "/home/mhonn/Data/markedupFiles/markedup_v1"
    buildIndex(inputMU)
    category = CCG.Category('((((S[dcl]\NP)/NP)/PP)/PP)/NP')
    CATEGORY.newCat(category)
    PROMPT.newCat(category)
    queue = findMatch(category)
    for cat in queue:
        print cat
    doQueue(queue)

    category.remaining = '(S[dcl]\NP)/(S[b]\NP)'
    category.annot = ''
    category.current = ''
    category.highlight('S[dcl]')
    category.addAnnot('S[dcl]{_}', True)
    category.highlight('NP')
    category.addAnnot('NP{Y}', True)
    category.highlight(r'(S[b]\NP)')
    category.addAnnot(r'(S[b]\NP){W}', False)
    category.highlight(r'S[b]')
    """

    
    

CATEGORY = None
HEADER = None
PROMPT = None
LOG = open('editMU.log', 'w')
muCats = {}
 
if __name__ == "__main__":
    import curses, curses.textpad
    if len(sys.argv) != 2:
        print "USAGE: editMarkedup.py <corpus>\nPlease ensure the screen is maximised, or you may get bugs."
        sys.exit(1)
    corpusLoc = sys.argv[1]
    inputMU = pjoin(corpusLoc, 'markedup')
    catsLoc = pjoin(corpusLoc, 'missingCats.txt')
    outputMU = pjoin(corpusLoc, 'markedup_additions.txt')
    try:
        curses.wrapper(main)
    finally:
        LOG.close()


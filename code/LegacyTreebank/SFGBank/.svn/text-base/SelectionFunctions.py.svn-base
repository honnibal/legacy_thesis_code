
"""
Specifies rules to select from systems

Each system is treated independently -- that is, its selection does not depend
on selections from other systems. The structure of the network is therefore
irrelevant to the rules.
"""
#import wntools, wordnet

def clauseClass(clause):
    """
    `Clause class' records whether the clause is a fragment
    
    Options: Major or Minor
    Major with Verbal Group
    Minor without Verbal Group
    """
    # If unfinished, probably junk. sw2010.mrg~0111
    if 'UNF' in clause.functionLabels:
        return 'minor'
    if clause.verbalGroup():
        return 'major'
    else:
        return 'minor'

def rank(clause):
    """
    Records whether the clause is ranking
    """
    if clause.isType('Ranking_Clause'):
        return 'ranking'
    else:
        return 'shifted'

def shiftType(clause):
    """
    Records whether the clause is embedded or nominalised
    """
    if clause.isType('Nominaised_Clause'):
        return 'nominal'
    else:
        return 'embedded'
        
def embedType(clause):
    """
    Records what type the clause modifies
    """
    parent = clause.parent()
    if parent.isType('Nominal_Group'):
        return 'nominal_qualifier'
    elif parent.isType('Adverbial_Group'):
        return 'adverbial_qualifier'
    else:
        return 'other_qualifier'

def polarity(clause):
    """
    Options: negative, positive
    if n't or not in verbal group: negative
    else: positive
    """
    for child in clause.children():
        if child.isType('Adverbial_Group'):
            if child.length() == 1:
                word = child.child(0)
                if word.isType('Word') and word.text.lower() in ["n't", 'not']:
                    return 'negative'
    if [word for word in clause.verbalGroup().listWords() if word.text.lower() in ["n't", 'not']]:
        return 'negative'
    else:
        return 'positive'
        
def negativeType(clause):
    """
    Records whether the negative is fused
    
    Options: combinedNegative, simpleNegative
    if n't or not in verbal group: negative
    else: positive
    """
    if [word for word in clause.verbalGroup().listWords() if word.text.lower() == "n't"]:
        return 'combined_negative'
    else:
        return 'simple_negative'
        
def status(clause):
    """
    `Status' records whether a clause is independent
    
    Options: free, bound
    if attached to the clause complex, free
    Otherwise, bound
    """
    if (not clause.interpersonal.finite) and (clause.interpersonal.predicator) and (clause.interpersonal.predicator[0].label in ['VBG', 'VBN', 'TO']):
        return 'bound'
    if clause.parent().isType('Clause_Complex'):
        return 'free'
    elif clause.quoted and clause.parent().parent().isType('Clause_Complex'):
        return 'free'
    elif 'IMP' in clause.verbalGroup().functionLabels:
        return 'free'
    else:
        return 'bound'
        
def moodType(clause):
    """
    Options: indicative, imperative
    if explicitly marked imperative: imperative
    else,
    if subject: indicative
    else: imperative
    """
    if 'IMP' in clause.functionLabels:
        return 'imperative'
    # subject: Indicative 
    if clause.interpersonal.subject:
        return 'indicative'
    # Sentences may be indicative without a subject, via mood presumption.
    # In SWBD corpus, this is especially common, and imperatives are
    # marked explicitly. To avoid referring to the corpus, check whether there
    # is a finite
    if clause.interpersonal.finite:
        return 'indicative'
    # else: Imperative
    else:
        return 'imperative'

def indicativeType(clause):
    """
    Options: interrogative, declarative
    If labelled SQ or SBARQ: interrogative
    else: declarative
    """
    # If clause labelled for interrogative: interrogative
    if clause.label in ['SQ', 'SBARQ']:
        return 'interrogative'
    elif "Q" in clause.functionLabels:
        return 'interrogative'
    else:
        return 'declarative'

def declarativeType(clause):
    """
    FIX ME
    """
    return 'non-exclamative'
    
def indicativeSubjectPresumption(clause):
    """
    If subject, explicit
    else, implicit
    """
    if clause.interpersonal.subject:
        return 'explicit_indicative_subject'
    else:
        return 'implicit_indicative_subject'
        
def subjectEllipsis(clause):
    if not clause.interpersonal.subject:
        print clause
    if clause.interpersonal.subject.hasEllipsis():
        return 'ellipsed_subject'
    else:
        return 'worded_subject'
        
def interrogativeType(clause):
    """
    Options: polar, wh
    If there are no wh elements before finite: polar
    else: wh
    """
    for group in clause.groups():
        # find a WH group
        if group.label.startswith('WH'):
            # Check whether it's before the finite
            if group < clause.interpersonal.finite:
                return 'wh'
    else:
        return 'polar'
        
def whStatus(clause):
    """
    I think an `echo wh-' is finite^wh -- `You asked him what?'
    
    Options: echo_wh, neutral_wh
    if finite^wh, echo_wh
    else neutral_wh
    """
    for group in clause.groups():
        # Stop after finite
        if group > clause.interpersonal.finite:
            break
        # find a WH group
        if group.label.startswith('WH'):
            return 'neutral_wh'
    return 'echo_wh'
        
def whSelection(clause):
    """
    Options: subject_wh, non-subject_wh
    if subject label is whnp: subject_wh
    else: non-subject_wh
    """
    if clause.interpersonal.subject and clause.interpersonal.subject.label == 'WHNP':
        return 'subject_wh'
    else:
        return 'non_subject_wh'
        
def whProjection(clause):
    """
    WH projection means WH extraction.
    
    Look for a clause child that has an empty WH trace
    """
    clauseChildren = [c for c in clause.children() if c.isType('Clause')]
    for child in clauseChildren:
        if child.label.startswith('WH') and child.children()[0].text == '0':
            return 'projected'
    return 'non-projected'
    
def nonSubjectWhSelection(clause):
    """
    Options: complement wh, adjunct wh
    if wh label is WHNP: complement wh
    else: adjunct wh
    """
    for group in clause.groups():
        # find the WH group
        if group.label == 'WHNP':
            return 'complement_wh'
        else:
            return 'adjunct_wh'
            
def indicativeMoodPerson(clause):
    """
    Options: interactant, non-interactant
    if subject is first or second person pronoun: interactant
    else: non-interactant
    """
    if clause.interpersonal.subject.getWord(0).text.lower() in ['i', 'you', 'we']:
        return 'interactant'
    else:
        return 'non-interactant'
        
def interactantType(clause):
    """
    Options: speaker, speaker-plus, addressee
    if i speaker
    if we speaker-plus
    if you addressee
    PROBLEM: speaker-plus is supposed to be inclusive we (you and me), not exclusive we (me and him).
    How to disambiguate?
    """
    if clause.interpersonal.subject.getWord(0).text.lower() == 'i':
        return 'speaker'
    elif clause.interpersonal.subject.getWord(0).text.lower() == 'we':
        return 'speaker_plus'
    else:
        return 'addressee'
    
def interrogativeMoodPresumption(clause):
    """
    FIX ME
    """
    pass
    

        
def deicticity(clause):
    """
    Options: modal finiteness, temporal finiteness
    if finite's POS is 'MD' and not will, shall, 'll: modal finiteness
    else: temporal finiteness
    """
    if (clause.interpersonal.finite.label == 'MD') and (clause.interpersonal.finite.text.lower() not in ['will', 'shall', "'ll"]):
        return 'modal'
    else:
        return 'temporal'
        

def primaryTense(clause):
    """
    Options: past, present, future
    if finite's POS is VBD or VBN: past
    if finite's POS is VB, VBG, VBZ or VBP: present
    if finite's POS is MD: future
    """
    if clause.interpersonal.finite.label in ['VBD', 'VBN']:
        return 'past'
    elif clause.interpersonal.finite.label in ['VB', 'VBG', 'VBZ', 'VBP']:
        return 'present'
    elif clause.interpersonal.finite.label == 'MD':
        return 'future'
    # Otherwise, guess
    elif clause.interpersonal.finite.text.endswith('ed'):
        return 'past'
    else:
        return 'present'
        
def imperativeType(clause):
    """
    FIX ME
    """
    return 'non-optative'
    
def imperativeMoodPerson(clause):
    """
    Options: oblative singular, oblative plural, jussive
    if no groups labelled subject: jussive
    if labelled subject is us or 's: suggestive
    if labelled subject is me: oblative
    if labelled subject anything else: jussive
    """
    # Retrieve labelled subjects
    labelledSubjects = [group for group in clause.groups() if 'SBJ' in group.functionLabels]
    if not labelledSubjects:
        return 'jussive'
    elif labelledSubjects[0].getWord(0).text.lower() in ['us', "'s"]:
        return 'suggestive'
    elif labelledSubjects[0].getWord(0).text.lower() == 'me':
        return 'oblative'
    else:
        return 'jussive'
        
def jussiveType(clause):
    """
    Options: explicit, implicit
    if there is a vocative: explicit
    else: implicit
    """
    if clause.interpersonal.vocative:
        return 'explicit_jussive_subject'
    else:
        return 'explicit_jussive_subject'
        
def tagging(clause):
    """
    FIX ME
    """
    pass

def tagPolarity(clause):
    """
    FIX ME
    """
    pass
    
def finiteness(clause):
    """
    Options: finite, non-finite
    if Finite, finite
    else, non-finite      
    """
    if clause.interpersonal.finite and clause.interpersonal.subject:
        return 'finite'
    else:
        return 'non-finite'
        
def vocative(clause):
    """
    Options: vocative, no vocative
    if Vocative, vocative
    else, no_vocative      
    """
    if clause.interpersonal.vocative:
        return 'vocative'
    else:
        return 'no_vocative'

def assessment(clause):
    """
    Records whether a clause has a comment adjunct
    """
    if clause.interpersonal.commentAdjunct:
        return 'assessed'
    else:
        return 'non-assessed'
    
def themeSelection(clause):
    """
    Options: marked, unmarked
    In non-finite or imperative clauses, predicator is unmarked
    otherwise, subject is
    """
    assert clause.textual.topicalTheme
    if clause.textual.topicalTheme.label.startswith('W'):
        return 'unmarked'
    if clause.interpersonal.subject:
        if clause.textual.topicalTheme == clause.interpersonal.subject:
            return 'unmarked'
        else:
            return 'marked'
    else:
        if clause.textual.topicalTheme == clause.verbalGroup():
            return 'unmarked'
        else:
            return 'marked'


def themeMatter(clause):
    """
    Options: as theme matter, as transitivity role
    Theme matter if PP with certain lexical patterns
    Otherwise, transitivity
    """
    if (clause.textual.topicalTheme.label == 'PP') and (not clause.textual.topicalTheme.functionLabels):
        themeString = ' '.join([word.text for word in clause.textual.topicalTheme.listWords()]).lower()
        themeMatterStrings = ['concerning', 'regarding', 'as to', 'as for']
        for realisation in themeMatterStrings:
            if themeString.startswith(realisation):
                return 'as_theme_matter'
    return 'as_transitivity_role'


def themeRole(clause):
    """
    Options: as process, as circumstance, as participant
    Match the topical theme with its interpersonal function
    """
    if clause.textual.topicalTheme.interpersonal.function == 'complement':
        return 'as_participant'
    elif clause.textual.topicalTheme.interpersonal.function == 'adjunct':
        return 'as_adjunct'
    elif clause.textual.topicalTheme == clause.verbalGroup():
        return 'as_process'
    else:
        raise StandardError, 'No transitivity role assignable for topical theme'
        

def themePredication(clause):
    """
    Options: predicated theme, non-predicated theme
    Look for a cleft-marked clause on the subject
    """
    for child in clause.interpersonal.subject.groups():
        if 'CLF' in child.functionLabels:
            return 'predicated_theme'
    return 'non-predicated_theme'
    
def thematicEquative(clause):
    """
    Records whether a clause is an equation between a nominalised Value and a
    non-nominalised Token
    
    Options: thematic_equative, no_thematic_equative
    """
    if len(clause.experiential.participant) != 2:
        return 'no_thematic_equative'
    # Test for a 'PRD' function label as a surrogate for proper relational process testing
    if 'PRD' not in clause.experiential.participant[1].functionLabels:
        return 'no_thematic_equative'
    nominalisations = [g for g in clause.experiential.participant if g.child(0).isType('Clause')]
    if len(nominalisations) < 1:
        return 'no_thematic_equative'
    elif len(nominalisations) > 1:
        return 'double_nominalisation'
    else:
        return 'single_nominalisation'
        
def nominalisationPosition(clause):
    """
    Records whether the nominalisation is theme (unmarked) or rheme (marked)
    """
    if clause.textual.topicalTheme.metadata.has_key('Nominalisation'):
        return 'as_theme'
    else:
        return 'as_rheme'

    
def localThemeSelection(clause):
    """
    FIX ME
    """
    return None
    for child in clause.interpersonal.subject.children():
        if 'CLF' in child.functionLabels:
            # Get subjects
            subjects = [group for group in child.children() if 'SBJ' in group.functionLabels]
            if not subjects:
                #  look for WHNP's 
                subjects = [group for group in child.children() if (group.label == 'WHNP')]
            ideationalGroups = []
            for group in child.children:
                group.discernConstituencyType()
                if group.constituentType in ['Nominal', 'Verbal', 'Adverbial', 'Prepositional']:
                    ideationalGroups.append(group)
            if subjects:
                if subjects[0] == ideationalGroups[0]:
                    return 'unmarked_local'
                else:
                    return 'marked_local'
            else:
                if ideationalGroups[0] == child.verbalGroup:
                    return 'unmarked_local'
                else:
                    return 'marked_local'

def conjunction(clause):
    """
    Records whether there is a conjunction in the clause
    """
    for group in clause.groups():
        if group.interpersonal.function == 'conjunctiveAdjunct':
            return 'conjuncted'
        elif group.isType('Conjunction_Group'):
            return 'conjuncted'
    return 'non-conjuncted'
                    
def textualTheme(clause):
    """
    Records whether a clause has a textual theme
    
    Options: textual_theme, no_textual_theme
    """
    if clause.textual.textualTheme:
        return 'textual_theme'
    else:
        return 'no_textual_theme'

def assessmentTheme(clause):
    """
    Records whether a clause has a comment adjunct theme
    """
    for theme in clause.textual.interpersonalTheme:
        if theme.interpersonal == 'commentAdjunct':
            return 'assessment_theme'
    return 'no_assessment_theme'

def vocativeTheme(clause):
    """
    Records whether a clause has a vocative theme
    """
    for theme in clause.textual.interpersonalTheme:
        if theme.interpersonal.function == 'vocative':
            return 'vocative_theme'
    return 'no_vocative_theme'
    
def agency(clause):
    """
    Options:
    effective, middle
    effective if at least one complement or passive
    otherwise middle      
    """
    if clause.interpersonal.complement:
        return 'effective'
    verbToBe = ['be', 'been', 'being', 'is', 'are', 'was', 'were']
    # If verbal group complex, use the first vg
    firstVG = clause.verbalGroup()
    while firstVG.isType('Complex'):
        firstVG = firstVG.child(0)
    verbalGroup = [l for l in firstVG.children() if l.isType('Word')]
    try:
        assert verbalGroup
    except:
        print clause.verbalGroup()
        assert verbalGroup
    if (len(verbalGroup) == 1):
        if verbalGroup[-1].label == 'VBN':
            return 'effective'
        else:
            return 'middle'
    else:
        if (verbalGroup[-2].text.lower() in verbToBe) and (verbalGroup[-1].label in ['VBN', 'VBD']):
            return 'effective'
        else:
            return 'middle'
        

def effectiveVoice(clause):
    """
    Options:
    operative, receptive
    operative is 'active' verbal group
    receptive is 'passive' verbal group
    """
    verbToBe = ['be', 'been', 'being', 'is', 'are', 'was', 'were']
    # If verbal group complex, use the first vg
    firstVG = clause.verbalGroup()
    while firstVG.isType('Complex'):
        firstVG = firstVG.child(0)
    verbalGroup = [l for l in firstVG.children() if l.isType('Word')]
    try:
        assert verbalGroup
    except:
        print clause.verbalGroup()
        assert verbalGroup
    if (len(verbalGroup) == 1):
        if verbalGroup[-1].label == 'VBN':
            return 'receptive'
        else:
            return 'operative'
    else:
        if (verbalGroup[-2].text.lower() in verbToBe) and (verbalGroup[-1].label in ['VBN', 'VBD']):
            return 'receptive'
        else:
            return 'operative'
        


def receptiveAgency(clause):
    """
    Options:
    agentive, non-agentive
    agentive has 'by' adjunct
    non-agentive does not
    """
    for adjunct in clause.interpersonal.adjunct:
        if (not adjunct.functionLabels) and (adjunct.listWords()[0].text.lower() == 'by'):
            return 'agentive'
    return 'non-agentive'

    
def secondaryOrBetaClause(clause):
    """
    Records whether the clause is an expansion/projection
    If the clause's parent is another clause, True (dependent)
    elif there's a sibling clause before it, True (co-ordinate)
    else, False
    """
    if clause.parent().isType('Clause'):
        return 'true'
    else:
        return 'false'

def taxis(clause):
    """
    If previous clause sibling, parataxis
    elif clause is quoted, parataxis
    elif clause's parent is a clause, hypotaxis
    else parataxis
    """
    coordinators = {'and': True, 'or': True, 'but': True}
    conjunctions = clause.textual.textualThemes
    for conjunction in conjunctions:
        for word in conjunction.listWords():
            if word.text.lower() in coordinators:
                return 'parataxis'
    if clause.quoted:
        return 'parataxis'
    else:
        return 'hypotaxis'
   # siblings = [s for s in clause.siblings() if s.isType('Clause')]
   # if (siblings) and (siblings[0] < clause):
   #     return 'parataxis'
   # elif clause.quoted:
   #     return 'parataxis'
   # elif clause.parent().isType('Clause'):
   #     return 'hypotaxis'
   # else:
   #     return 'parataxis'
        
def interdependencyType(clause):
    if 'SBARQ' in clause.functionLabels:
        return 'projection_clause'
    elif 'SBAR' in clause.functionLabels:
        return 'projection_clause'
    elif ' '.join([t.text for t in clause.groups()[0].listWords()]).lower() == 'that':
        return 'projection_clause'
    elif clause.quoted:
        return 'projection_clause'
    elif 'TPC' in clause.functionLabels:
        return 'projection_clause'
    elif clause.functionLabels:
        return 'expansion_clause'
    elif clause.textual.textualThemes:
        return 'expansion_clause'
    else:
        return 'projection_clause'
        
def expansionClauseType(clause):
    """
    Options: elaborating, extending, enhancing
    if relative/reduced relative, elaborating
    if rankshifted and not relative/reduced relative, enhancing
    if specific adverbial tag, enhancing
    if ranking and -ADV tag, extending
    if ranking and unmarked participle, extending
    """ 
    # If ellipsed, extending
    if clause.hasEllipsis():
        return 'extending_clause'
    # If relative, elaborating
    if clause.group(0).label in ['WHADJP', 'WHNP', 'WHPP']:
        return 'elaborating_clause'
    elif clause.group(0).label == 'WHADVP':
        return 'enhancing_clause'
    # elif reduced relative, elaborating
    elif clause.label == 'RRC':
        return 'elaborating_clause'
    # elif rankshifted, enhancing
    elif not clause.isType('Ranking_Clause'):
        return 'enhancing_clause'
    # elif specific adverbial label, enhancing
    elif [adverbialLabel for adverbialLabel in clause.functionLabels if adverbialLabel in ['BNF', 'DIR', 'EXT', 'LOC', 'LOC', 'PRP', 'TMP']]:
        return 'enhancing_clause'
    elif clause.parent().isType('Clause'):
        return 'enhancing_clause'
    # elif generic adverbial label, extending
    elif 'ADV' in clause.functionLabels:
        return 'extending_clause'
    # elif unlabelled participle, extending
    elif (clause.interpersonal.predicator) and (not clause.interpersonal.finite) and (clause.interpersonal.predicator[0].label in ['VBN', 'VBG']):
        return 'extending_clause'
    elif clause.label == 'SBAR':
        return 'enhancing_clause'
    elif 'SBAR' in clause.functionLabels:
        return 'enhancing_clause'
    # If left sibling is clause, extending
    lSibling = clause.sibling(-1)
    if (lSibling) and (lSibling.isType('Clause')):
        return 'extending_clause'
    # If no parent clause, and conjunction extending
    elif (clause.parent().isType("Clause_Complex")) and (not lSibling) and (clause.child(0).label == 'CONJP'):
        return 'extending_clause'
    else:
        if 'SBAR' in clause.functionLabels:
            return 'enhancing_clause'
        else:
            return 'extending_clause'

def section(clause):
    """
    Shouldnt be called
    """
    raise StandardError

        
"""
Word Rank
"""
"""
def partOfSpeech(word):
    if word.label.startswith('N'):
        return 'noun'
    elif word.label.startswith('V'):
        return 'verb'
    elif word.label == 'JJ':
        return 'adjective'
    elif word.label.startswith('R'):
        return 'adverb'
    else:
        return 'other'
        
def possessor(word):
    # Try for a 's possessive
    if word.possession.possessed:
        return 'true'
    else:
        return 'false'
            
def possessionType(word):
    siblings = [c for c in word.parent().children() if c.isType('Word')]
    if word != siblings[-1]:
        return 'genitive_possessor'
    else:
        return 'of_possessor'
        
def possessorWordnetEntry(word):
    senses = word.metadata.get('senses', [])
    if senses:
        return 'true'
    else:
        return 'false'
        
def possessorSyntaxEntry(word):
    syntax = word.metadata.get('COMLEX', [])
    if syntax:
        return 'true'
    else:
        return 'false'
        
def possessorSenseAmbiguity(word):
    if len(word.metadata['senses']) > 1:
        return 'multiple_senses'
    else:
        return 'single_sense'
  
def possessorPropriety(word):
    if word.label in ['NNP', 'NNPS']:
        return 'proper_noun'
    else:
        return 'common_noun'
        
def possessorCountability(word):
    entry = word.metadata['COMLEX'][0]
    if entry.hasFeature('COUNTABLE'):
        return 'countable'
    else:
        return 'uncountable'
        
def possessorConcreteness(word):
    global ENTITY
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if ENTITY in hypernyms:
        return 'concrete'
    else:
        return 'abstract'
        
def possessorAnimacy(word):
    global ANIMATE_THING 
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if ANIMATE_THING in hypernyms:
        return 'animate'
    else:
        return 'inanimate'
        
def possessorGrouping(word):
    global GROUPING
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if GROUPING in hypernyms:
        return 'aggregate'
    else:
        return 'single'

def possessedWordnetEntry(word):
    word = word.possession.possessed
    senses = word.metadata.get('senses', [])
    if senses:
        return 'true'
    else:
        return 'false'
        
def possessedSyntaxEntry(word):
    word = word.possession.possessed
    syntax = word.metadata.get('COMLEX', [])
    if syntax:
        return 'true'
    else:
        return 'false'
        
def possessedSenseAmbiguity(word):
    word = word.possession.possessed
    if len(word.metadata['senses']) > 1:
        return 'multiple_senses'
    else:
        return 'single_sense'
  
def possessedPropriety(word):
    word = word.possession.possessed
    if word.label in ['NNP', 'NNPS']:
        return 'proper_noun'
    else:
        return 'common_noun'
        
def possessedCountability(word):
    word = word.possession.possessed
    entry = word.metadata['COMLEX'][0]
    if entry.hasFeature('COUNTABLE'):
        return 'countable'
    else:
        return 'uncountable'
        
def possessedConcreteness(word):
    global ENTITY
    word = word.possession.possessed
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if ENTITY in hypernyms:
        return 'concrete'
    else:
        return 'abstract'
        
def possessedAnimacy(word):
    global ANIMATE_THING
    word = word.possession.possessed 
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if ANIMATE_THING in hypernyms:
        return 'animate'
    else:
        return 'inanimate'
        
def possessedGrouping(word):
    global GROUPING
    word = word.possession.possessed
    hypernyms = wntools.hypernyms(word.metadata['senses'][0])
    if GROUPING in hypernyms:
        return 'aggregate'
    else:
        return 'single'
"""
"""        
ENTITY = wordnet.N['entity'][0].synset
ANIMATE_THING = wordnet.N['animate thing'][0].synset
GROUPING = wordnet.N['grouping'][0].synset
"""

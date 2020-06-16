string1 = open('/home/mhonn/Data/CCGBank/PropMod/00/wsj_0003.auto').read()
string2 = open('/home/mhonn/Data/CCGBank/PropModTest/00/wsj_0003.auto').read()
print len(string1)
print len(string2)
print string1 == string2
i = 0
for c1, c2 in zip(string1, string2):
    if c1 != c2:
        print c1
        print c2
        print i
        print string1[i-100:i+20]
        print string2[i-100:i+20]
        break
    i += 1

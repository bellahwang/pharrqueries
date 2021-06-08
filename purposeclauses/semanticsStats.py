# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

# change FILENAME to local path
FILENAME = "iliad_purposeclauses_v2.xml"

def subjOpt():
    tree = ET.parse(FILENAME)
    root = tree.getroot()

    subjcount = 0
    optcount = 0
    othercount = 0
    debugcount = 0

    for sentence in root.findall(".//sentence"):
        verbid = 1000001
        conjhead = 1000002

        for word in sentence.findall("./word"):
            lemma = word.get('lemma')
            
            if ('postag' in word.attrib):
                postag = word.get('postag')
                pos = postag[0]

                if (lemma == "ἵνα" or lemma == "ὅπως" or lemma == "ὡς" or lemma == "μή" or lemma == "ὄφρα" or lemma == "ἕως"):
                    conjhead = word.get('head')
                elif (pos == 'v'):
                    verbmood = "debug"
                    verbid = word.get('id')
                    verbmood = postag[4]

                if (conjhead == verbid):
                    if (verbmood == 'o'): # optative
                        optcount += 1
                    elif (verbmood == 's'): # subjunctive
                        subjcount += 1
                    elif (verbmood == 'debug'): #picking up the wrong thing
                        debugcount += 1
                    else:
                        othercount += 1

    print("optative verbs depending on purpose clause conjunctions: ", optcount)
    print("subjunctive verbs depending on purpose clause conjunctions: ", subjcount)
    print("verbs that are neither optative nor subjunctive depending on purpose clause conjunctions: ", othercount)
    print("errors: ", debugcount)

def conjNoDepend():
    tree = ET.parse(FILENAME)
    root = tree.getroot()

    noDependCount = 0

    for sentence in root.findall(".//sentence"):
        wordid = 1000001
        conjhead = 1000002
        
        conjDepend = False

        for word in sentence.findall("./word"):
            lemma = word.get('lemma')
            if (lemma == "ἵνα" or lemma == "ὅπως" or lemma == "ὡς" or lemma == "μή" or lemma == "ὄφρα" or lemma == "ἕως"):
                conjhead = word.get('head')
            else:
                wordid = word.get('id')

            if (conjhead == wordid):
                conjDepend = True
        
        if (conjDepend == False):
            noDependCount += 1
    
    print("# of conjunctions that do not have anything depending on them: ", noDependCount)

subjOpt()
print()
conjNoDepend()
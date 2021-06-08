# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import os.path
import yaml

# change FILENAME to local path
FILENAME = "iliad_purposeclauses_v2.xml"

def makeIdDict(givenSentID):
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    IdDict = {}
    
    for sentence in root.findall(".//sentence"):
        loopingSentID = sentence.get('id')
        if (loopingSentID == givenSentID):
            for word in sentence.findall("./word"):
                form = word.get('form')
                wordID = word.get('id')
                IdDict[wordID] = form
            
    return IdDict

def makeHeadDict(givenSentID):
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    HeadDict = {}
    
    for sentence in root.findall(".//sentence"):
        loopingSentID = sentence.get('id')
        if (loopingSentID == givenSentID):
            for word in sentence.findall("./word"):
                form = word.get('form')
                wordHead = word.get('head')
                HeadDict[form] = wordHead
    
    return HeadDict

def matchDicts(IdDict, HeadDict):
    #MatchedDict = {}
    
    IdFormList = returnIdFormList(IdDict)
    HeadFormList = returnHeadFormList(IdDict, HeadDict)
    MatchedDict = dict(zip(IdFormList, HeadFormList))
    #print(MatchedDict.items(), sep = '\n')

    return MatchedDict
    
def returnIdFormList(IdDict):
    IdFormList = []
    for x in IdDict:
        IdForm = IdDict[x]
        IdFormList.append(IdForm)
        IdForm = None
    return IdFormList

def returnHeadFormList(IdDict, HeadDict):
    HeadFormList = []
    for x in IdDict:
        IdForm = IdDict[x]
        head = HeadDict[IdForm]
        if(head != '0'):
            headForm = IdDict[head]
            HeadFormList.append(headForm)
            headForm = None
    return HeadFormList

""" def createNetwork(matchedDict, sentID):
    sent = matchedDict[sentID]
    G = nx.DiGraph()
    for idlemma in sent:
        headlemma = sent[idlemma]
        G.add_edge(idlemma, headlemma)
    return G """

""" def createGraphMLs(matchedDict):
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    save_path = 'C:\\Users\\bella\\OneDrive\\Documents\\GitHub\\pharrqueries\\purposeclauses\\Iliad'
    
    for sentence in root.findall(".//sentence"):
        sentID = sentence.get('id')
        G = createNetwork(matchedDict, sentID)
        name_of_file = "Iliad" + sentID + "pc"
        completeName = os.path.join(save_path, name_of_file + ".graphml") 
        nx.write_graphml(G, completeName) """

def nodeMaker(givenSentID):
    G = nx.MultiDiGraph()

    tree = ET.parse(FILENAME)
    root = tree.getroot()

    for sentence in root.findall(".//sentence"):
        loopingSentID = sentence.get('id')
        if (loopingSentID == givenSentID):
            for word in sentence.findall("./word"):
                wordID = word.get('id')
                wordForm = word.get('form')
                wordLemma = word.get('lemma')
                wordHead = word.get('head')
                wordRelation = word.get('relation')
                if ('postag' in word.attrib):
                    wordPostag = word.get('postag')
                    wordCite = word.get('cite')
                    G.add_node(wordForm, id = wordID, form = wordForm, lemma = wordLemma, postag = wordPostag, head = wordHead, relation = wordRelation, cite = wordCite)
                else:
                    G.add_node(wordForm, id = wordID, form = wordForm, head = wordHead, relation = wordRelation)
                
                wordID = None
                wordForm = None
                wordLemma = None
                wordHead = None
                wordRelation = None
                wordPostag = None
                wordCite = None
    return G

def edgeMaker(G, MatchedDict, givenSentID):
    
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for sentence in root.findall(".//sentence"):
        loopingSentID = sentence.get('id')
        if (loopingSentID == givenSentID):
            for word in sentence.findall("./word"):
                wordForm = word.get('form')
                wordRelation = word.get('relation')
                if (wordForm in MatchedDict):
                    isDependentOn = MatchedDict[wordForm]
                    G.add_edge(isDependentOn, wordForm, relation = wordRelation)
    return G

IdDict = makeIdDict('2274118')
HeadDict = makeHeadDict('2274118')

MatchedDict = matchDicts(IdDict, HeadDict)

G = nodeMaker('2274118')
H = edgeMaker(G, MatchedDict, '2274118')
nx.write_graphml(H, 'debug.graphml', encoding = 'UTF-8', prettyprint = True)


# print(yaml.dump(MatchedDict, allow_unicode=True, default_flow_style=False))
# createGraphMLs(MatchedDict)
nx.draw(H)
# print(returnIdLemmaList(IdDict, '2274115'))
# print(returnHeadLemmaList(IdDict, HeadDict, '2281055'))
import xml.etree.ElementTree as ET
import networkx as nx

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.read_graphml("test.graphml")

# def returnHeadList(givensentid):
# headlist = []
# for sentence in root.findall(".//sentence"):
# 	givensentid = '2274107'
# 	sentid = sentence.get('id')
# 	if (sentid == givensentid):
# 		for word in sentence.findall("./word"):
# 			head = word.get('head')
# 			headlist.append(head)

# print(headlist)

# def returnIDList(givensentid):
# IDlist = []
# for sentence in root.findall(".//sentence"):
# 	givensentid = '2274107'
# 	sentid = sentence.get('id')
# 	if (sentid == givensentid):
# 		for word in sentence.findall("./word"):
# 			id = word.get('id')
# 			IDlist.append(id)
# print(IDlist)

# def returnLemmaList(givensentid):
# Lemmalist = []
# for sentence in root.findall(".//sentence"):
# 	givensentid = '2274107'
# 	sentid = sentence.get('id')
# 	if (sentid == givensentid):
# 		for word in sentence.findall("./word"):
# 			lemma = word.get('lemma')
# 			Lemmalist.append(lemma)
# print(Lemmalist)

# def returnRelationList(givensentid):
Relationlist = []
for sentence in root.findall(".//sentence"):
	givensentid = '2274107'
	sentid = sentence.get('id')
	if (sentid == givensentid):
		for word in sentence.findall("./word"):
			relation = word.get('relation')
			Relationlist.append(relation)
print(Relationlist[0])

# for sentence in root.findall(".//sentence"):
# 	sentid = '2274107'
# 	headlist = returnHeadList(sentid)
# 	IDlist = returnIDList(sentid)
# 	Lemmalist = returnLemmaList(sentid)
# 	Relationlist = returnRelationList(sentid)

# 	for i in range(len(IDlist)):
# 		lemma1 = Lemmalist[i]
# 		for j in range(len(headlist)):
# 			lemma2 = Lemmalist[j]
# 			if i == j:
# 				relation = Relationlist[j]
# 				if G.has_edge(lemma2, lemma1):
# 					G[lemma2][lemma1]['weight'] += 1
# 				else:
# 					G.add_edge(lemma2, lemma1, relation = relation, weight = 1)

# nx.write_graphml(G, "iliadNetwork.graphml")


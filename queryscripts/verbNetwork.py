import xml.etree.ElementTree as ET
import networkx as nx

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.DiGraph()

verbid = None
attribhead = None

for sentence in root.findall(".//sentence"):
	for word in sentence.findall("./word"):
		if ('postag' in word.attrib):
			postag = word.get('postag')
			pos = postag[0]
		if ('relation' in word.attrib):
			relation = word.get('relation')
			if (relation == 'PRED' or relation == 'PRED_CO' and pos == 'v'):
				verbid = word.get('id')
				verblemma = word.get('lemma')
				verbform = word.get('form')
				G.add_node(verblemma, pos = pos)
			else:
				attribrelation = word.get('relation')
				if (attribrelation == 'SBJ' or attribrelation == 'SBJ_CO'):
					attribhead = word.get('head')
					attriblemma = word.get('lemma')
					attribcite = word.get('cite')
					G.add_node(attriblemma, pos = pos)
					if (attribhead == verbid and attriblemma != None):
						# if G.has_edge(verblemma, attriblemma):
						# 	G[verblemma][attriblemma]['weight'] += 1
						# else:
						# 	G.add_edge(verblemma, attriblemma, relation = attribrelation, weight = 1)
						if G.has_edge(attriblemma, verblemma):
							G[attriblemma][verblemma]['weight'] += 1
						else:
							G.add_edge(attriblemma, verblemma, relation = attribrelation, weight = 1)

nx.write_graphml(G, "CONJPNOM.graphml")

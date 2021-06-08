import xml.etree.ElementTree as ET
import networkx as nx

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.DiGraph()

prepid = None
preplemma = None
attribhead = None

for sentence in root.findall(".//sentence"):
	for word in sentence.findall("./word"):
		if ('postag' in word.attrib):
			postag = word.get('postag')
			pos = postag[0]
			if (pos == 'r'):
				prepid = word.get('id')
				preplemma = word.get('lemma')
				G.add_node(preplemma, pos = pos)
			else:
				attribrelation = word.get('relation')
				# if (attribrelation == 'PNOM' or attribrelation == 'SBJ'):
				attribhead = word.get('head')
				attriblemma = word.get('lemma')
				if (attribhead == prepid):
					
					G.add_node(attriblemma, lemma = attriblemma, pos = pos, connectedWith = preplemma)
					
					# if (attribrelation):
					# 	if G.has_edge(preplemma, attriblemma):
					# 		G[preplemma][attriblemma]['weight'] += 1
					# 	else:
					# 		G.add_edge(preplemma, attriblemma, relation = attribrelation, weight = 1)
                    # else:
					if G.has_edge(attriblemma, preplemma):
						G[attriblemma][preplemma]['weight'] += 1
					else:
						G.add_edge(attriblemma, preplemma, relation = attribrelation, weight = 1)

nx.write_graphml(G, "prepNetwork.graphml")
# nx.draw(G)
# plt.show()

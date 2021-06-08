import xml.etree.ElementTree as ET
import networkx as nx

# change FILENAME to local path
FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"

tree = ET.parse(FILENAME)
root = tree.getroot()

G = nx.DiGraph()

prepid = 10001
preplemma = 10002
objhead = 10003
objlemma = 10004
objform = 10005
objcase = 10006


for sentence in root.findall(".//sentence"):
    for word in sentence.findall("./word"):
        if ('postag' in word.attrib):
            postag = word.get('postag')
            pos = postag[0]
            if (pos == 'r'):
                prepid = word.get('id')
                preplemma = word.get('lemma')
                if (objhead == prepid):
                    if G.has_node(objlemma):
                        if objcase == 'g':
                            G.nodes[objlemma].update({'gen': 0})
                            temp = G.nodes[objlemma]['gen']
                            temp += 1
                            G.nodes[objlemma].update(gen = temp)
                        if objcase == 'd':
                            G.nodes[objlemma].update({'dat': 0})
                            temp = G.nodes[objlemma]['dat']
                            temp += 1
                            G.nodes[objlemma].update(dat = temp)
                        if objcase == 'a':
                            G.nodes[objlemma].update({'acc': 0})
                            temp = G.nodes[objlemma]['acc']
                            temp += 1
                            G.nodes[objlemma].update(acc = temp)
                        if objcase == 'n':
                            G.nodes[objlemma].update({'nom': 0})
                            temp = G.nodes[objlemma]['nom']
                            temp += 1
                            G.nodes[objlemma].update(nom = temp)
                        if objcase == 'v':
                            G.nodes[objlemma].update({'voc': 0})
                            temp = G.nodes[objlemma]['voc']
                            temp += 1
                            G.nodes[objlemma].update(voc = temp)
                        temp = G.nodes[objlemma]['weight']
                        temp += 1
                        G.nodes[objlemma].update(weight = temp)
                    else:
                        G.add_node(objlemma, pos = pos, weight = 0)
                    
                    if G.has_edge(objlemma, preplemma):
                        G[objlemma][preplemma]['weight'] += 1
                    else:
                        G.add_edge(objlemma, preplemma, weight = 1)
                
                if G.has_node(preplemma):
                    if objcase == 'g':
                        G.nodes[preplemma].update({'gen': 0})
                        temp = G.nodes[preplemma]['gen']
                        temp += 1
                        G.nodes[preplemma].update(gen = temp)
                    if objcase == 'd':
                        G.nodes[preplemma].update({'dat': 0})
                        temp = G.nodes[preplemma]['dat']
                        temp += 1
                        G.nodes[preplemma].update(dat = temp)
                    if objcase == 'a':
                        G.nodes[preplemma].update({'acc': 0})
                        temp = G.nodes[preplemma]['acc']
                        temp += 1
                        G.nodes[preplemma].update(acc = temp)
                    if objcase == 'n':
                        G.nodes[preplemma].update({'nom': 0})
                        temp = G.nodes[preplemma]['nom']
                        temp += 1
                        G.nodes[preplemma].update(nom = temp)
                    if objcase == 'v':
                        G.nodes[preplemma].update({'voc': 0})
                        temp = G.nodes[preplemma]['voc']
                        temp += 1
                        G.nodes[preplemma].update(voc = temp)
                    temp = G.nodes[preplemma]['weight']
                    temp += 1
                    G.nodes[preplemma].update(weight = temp)
                else:
                    G.add_node(preplemma, pos = pos, weight = 0)

            elif (pos == 'n'):
                objhead = word.get('head')
                objlemma = word.get('lemma')
                objform = word.get('form')
                objpostag = word.get('postag')
                objcase = objpostag[7]
                if (objhead == prepid):
                    if G.has_node(objlemma):
                        if objcase == 'g':
                            G.nodes[objlemma].update('gen', 0)
                            temp = G.nodes[objlemma]['gen']
                            temp += 1
                            G.nodes[objlemma].update(gen = temp)
                        if objcase == 'd':
                            G.nodes[objlemma].update('dat', 0)
                            temp = G.nodes[objlemma]['dat']
                            temp += 1
                            G.nodes[objlemma].update(dat = temp)
                        if objcase == 'a':
                            G.nodes[objlemma].update('acc', 0)
                            temp = G.nodes[objlemma]['acc']
                            temp += 1
                            G.nodes[objlemma].update(acc = temp)
                        if objcase == 'n':
                            G.nodes[objlemma].update('nom', 0)
                            temp = G.nodes[objlemma]['nom']
                            temp += 1
                            G.nodes[objlemma].update(nom = temp)
                        if objcase == 'v':
                            G.nodes[objlemma].update('voc', 0)
                            temp = G.nodes[objlemma]['voc']
                            temp += 1
                            G.nodes[objlemma].update(voc = temp)
                        temp = G.nodes[objlemma]['weight']
                        temp += 1
                        G.nodes[objlemma].update(weight = temp)
                    else:
                        G.add_node(objlemma, pos = pos, weight = 0)
                    
                    if G.has_edge(objlemma, preplemma):
                        G[objlemma][preplemma]['weight'] += 1
                    else:
                        G.add_edge(objlemma, preplemma, weight = 1)
    prepid = 10001
    preplemma = 10002
    objhead = 10003
    objlemma = 10004
    objform = 10005
    objcase = 10006
nx.write_graphml(G, "2021427prepNetwork.graphml")

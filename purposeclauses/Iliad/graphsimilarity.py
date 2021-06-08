# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

# change FILENAME to local path
FILENAME1 = "Iliad2274115pc.graphml"
FILENAME2 = "Iliad2274118pc.graphml"

G1 = nx.read_graphml(FILENAME1)
G2 = nx.read_graphml(FILENAME2)

nx.draw(G1)
plt.draw()
import networkx as nx
import pylab as plt
import pandas as pd

G = nx.DiGraph()

df_sec_relation = pd.read_csv('section_relation.csv')
vv = df_sec_relation.values

for i in range(50):
    G.add_edge(vv[i][0], vv[i][1])

nx.draw(G, with_lables=True, node_size=40)

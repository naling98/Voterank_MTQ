import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def show_graph(adjList):
    gr = nx.Graph()
    gr.add_edges_from(adjList);
    nx.draw(gr, node_size = 20);
    plt.show();

mydata = np.genfromtxt('data.txt')
mydata = [[int(y) for y in x] for x in mydata]
mydata = [y for y in mydata if y[0]%4 == 0 and y[1]%4==0];
print(len(mydata));
show_graph(mydata);



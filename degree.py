import networkx as nx
import pandas as pd
from edge_generator import edgeGenerator
import matplotlib.pyplot as plt

df = pd.read_csv('data\\sample_delays_only_b.csv')

edge_list = edgeGenerator(df)  

G = nx.Graph()
G.add_nodes_from(df['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)
degrees = list(nx.degree(G))

# create and fill array for degrees
degrees_array = []
for i in range(201):
    degrees_array.append([i,0])

# count how much nodes have the same degree
for i in range(len(degrees)):
    degrees_array[degrees[i][1]][1] += 1

# remove first item and elements which value = 0 
degrees_array.pop(0)

i=199
while (i>0):
    if degrees_array[i][1] == 0:
        degrees_array.pop(i)
    i -= 1

# control print array in console
print(degrees_array)

# split values to x and y values
x , y = [], []

for i in degrees_array:
    x.append(i[0])
    y.append(i[1])


# plot results
plt.plot(x,y,'-b')
plt.plot(x,y,'or')
plt.show()
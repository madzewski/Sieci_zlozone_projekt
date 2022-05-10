from platform import node
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from edge_generator import edgeGenerator
import random

df = pd.read_csv('data\\sample_delays_only_b.csv')

edge_list = edgeGenerator(df)

G = nx.Graph()
G.add_nodes_from(df['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)
# nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()

# def delete_random_edges(G):
#     for i in range(1):
#         edge_list = list(G.edges())
#         u,v = random.choice(edge_list)
#         if G.degree(u) == 1 or G.degree(v) == 1:
#         G.remove_edge(u,v)



 

# def analysis(ix):

#     delete_random_edges(G)

#     if nx.is_connected(G):
#         print("\nStatystyki sieci ",ix,": ")
#         print('Średnica: ',nx.diameter(G))
#         print('Gęstość: ',nx.density(G))
#         print('Ilość wierzchołków: ',G.number_of_nodes())
#         print('Rozmiar: ',G.size())
#         print("Średnie gronowanie: ", nx.average_clustering(G))

#         edge_cen = pd.DataFrame.from_dict(nx.edge_betweenness_centrality(G), orient='index')
#         cols_1 = ['EDGE_BETWEENNESS_CENTRALITY']
#         edge_cen.columns = cols_1
#         print('\nTop 10 połączeń z największym współczynnikiem centralności:\n\n',edge_cen.sort_values(by='EDGE_BETWEENNESS_CENTRALITY', ascending=False).head(3).reset_index())

#         st_cen = pd.DataFrame.from_dict(nx.degree_centrality(G), orient='index')
#         cols_2 = ['DEGREE_CENTRALITY']
#         st_cen.columns = cols_2
#         print('\nTop 10 lotnisk z największym współczynnikiem centralności:\n\n',st_cen.sort_values(by='DEGREE_CENTRALITY', ascending=False).head(3).reset_index())

#         st = pd.DataFrame(nx.degree(G))
#         cols_4 = ['AIRPORT', 'CONNECTIONS']
#         st.columns = cols_4
#         print('\nTop 10 lotnisk z największą ilością połączeń:\n\n',st.sort_values(by='CONNECTIONS', ascending=False).head(3).reset_index())
#         return 0
#     else:
#         return 1
def delete_random_edges(G):
    counter = 0
    while True:
        edge_list = list(G.edges())
        u,v = random.choice(edge_list)
        if G.degree(u) != 1 and G.degree(v) != 1:
            G.remove_edge(u,v)
        counter += 1
        if not nx.is_connected(G):
            G.add_edge(u,v)
            break
    print(counter)
    
            

def analysis(ix):

    delete_random_edges(G)


    print("\nStatystyki sieci ",ix,": ")
    print('Średnica: ',nx.diameter(G))
    print('Gęstość: ',nx.density(G))
    print('Ilość wierzchołków: ',G.number_of_nodes())
    print('Rozmiar: ',G.size())
    print("Średnie gronowanie: ", nx.average_clustering(G))

    edge_cen = pd.DataFrame.from_dict(nx.edge_betweenness_centrality(G), orient='index')
    cols_1 = ['EDGE_BETWEENNESS_CENTRALITY']
    edge_cen.columns = cols_1
    print('\nTop 10 połączeń z największym współczynnikiem centralności:\n\n',edge_cen.sort_values(by='EDGE_BETWEENNESS_CENTRALITY', ascending=False).head(3).reset_index())

    st_cen = pd.DataFrame.from_dict(nx.degree_centrality(G), orient='index')
    cols_2 = ['DEGREE_CENTRALITY']
    st_cen.columns = cols_2
    print('\nTop 10 lotnisk z największym współczynnikiem centralności:\n\n',st_cen.sort_values(by='DEGREE_CENTRALITY', ascending=False).head(3).reset_index())

    st = pd.DataFrame(nx.degree(G))
    cols_4 = ['AIRPORT', 'CONNECTIONS']
    st.columns = cols_4
    print('\nTop 10 lotnisk z największą ilością połączeń:\n\n',st.sort_values(by='CONNECTIONS', ascending=False).head(3).reset_index())



# check = 0
# ix = 0
# while check != 1:
#     check = analysis(ix)
#     ix += 1
analysis(0)
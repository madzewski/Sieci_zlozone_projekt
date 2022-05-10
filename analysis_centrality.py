import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from edge_generator import edgeGenerator

df = pd.read_csv('data\\sample_delays_only_alaska.csv')

edge_list = edgeGenerator(df)

G = nx.Graph()
G.add_nodes_from(df['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)
# nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()

history=[]
def delete_top_edges(G,edge_list,n):
    for i in range(n):
        G.remove_edge(edge_list[i][0],edge_list[i][1])
        history.append([edge_list[i][0],edge_list[i][1]])

def analysis(n,ix):
    edge_cen = pd.DataFrame.from_dict(nx.edge_betweenness_centrality(G), orient='index')
    cols_1 = ['EDGE_BETWEENNESS_CENTRALITY']
    edge_cen.columns = cols_1
    edge_cen = edge_cen.sort_values(by='EDGE_BETWEENNESS_CENTRALITY', ascending=False).head(n).reset_index()
    edge_list = list(edge_cen['index'])

    delete_top_edges(G,edge_list,n)

    if nx.is_connected(G):
        print("\nStatystyki sieci ",ix," : ")
        # print('Średnica: ',nx.diameter(G))
        # print('Gęstość: ',nx.density(G))
        print('Ilość wierzchołków: ',G.number_of_nodes())
        print('Rozmiar: ',G.size())
        # print("Średnie gronowanie: ", nx.average_clustering(G))


        # print('\nTop 10 połączeń z największym współczynnikiem centralności:\n\n',edge_cen.sort_values(by='EDGE_BETWEENNESS_CENTRALITY', ascending=False).head(10).reset_index())

        st_cen = pd.DataFrame.from_dict(nx.degree_centrality(G), orient='index')
        cols_2 = ['DEGREE_CENTRALITY']
        st_cen.columns = cols_2
        # print('\nTop 10 lotnisk z największym współczynnikiem centralności:\n\n',st_cen.sort_values(by='DEGREE_CENTRALITY', ascending=False).head(10).reset_index())

        st = pd.DataFrame(nx.degree(G))
        cols_4 = ['AIRPORT', 'CONNECTIONS']
        st.columns = cols_4
        print('\nTop 10 lotnisk z największą ilością połączeń:\n\n',st.sort_values(by='CONNECTIONS', ascending=False).head(10).reset_index())
        return 0
    else:
        return 1


check = 0
ix = 0
while check != 1:
    check = analysis(1,ix)
    ix += 1

# for j in range(0,len(history),2):
#     print(j,history[j],' ',j+1,history[j+1])

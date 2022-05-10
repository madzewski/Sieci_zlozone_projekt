import pandas as pd 

def edgeGenerator(df):
    edge_list=[]

    for i in range(len(df)):
        if [df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']] not in edge_list and [df.iloc[i]['DESTINATION_AIRPORT'],df.iloc[i]['ORIGIN_AIRPORT']] not in edge_list:
            edge_list.append([df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']])
    
    return edge_list
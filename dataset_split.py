import pandas as pd
from pandas.core import indexing


alaska_air = ['ADK','ADQ','AKN','ANC','BET','BRW','CDV','DLG','FAI','GST','JNU','KTN','OME','OTZ','PSG','SCC','SIT','WRG','YAK']
df = pd.read_csv('data\\delays_only.csv')
# df = df.drop(columns=['FLIGHT_NUMBER', 'TAIL_NUMBER', 'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME', 'TAXI_OUT', 'WHEELS_OFF', 'SCHEDULED_TIME', 'ELAPSED_TIME', 'AIR_TIME', 'WHEELS_ON',
#              'TAXI_IN', 'SCHEDULED_ARRIVAL', 'ARRIVAL_TIME', 'DIVERTED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY', 'CANCELLED'])
# df = df.reset_index()
# 
df = df[~df.ORIGIN_AIRPORT.isin(alaska_air)]
df = df[~df.DESTINATION_AIRPORT.isin(alaska_air)]
df = df.drop(columns=['Unnamed: 0'])
print(df.head())
df.to_csv('data\\delays_only_alaska.csv')
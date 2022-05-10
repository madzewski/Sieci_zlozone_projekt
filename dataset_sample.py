import pandas as pd

df = pd.read_csv('data\\delays_only_alaska.csv')
df = df.sample(n=100000, random_state=254295).sort_index().reset_index()
df = df.drop(columns=['Unnamed: 0', 'index'])

df.to_csv('data\\sample_delays_only_alaska.csv')

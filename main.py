import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
s_data=pd.read_csv("Spotify_data.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
s_data.drop(columns=['Unnamed: 0'], inplace=True)
features=['Energy', 'Valence', 'Danceability', 'Loudness', 'Acousticness']
for feature in features:
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=s_data, x=feature, y='Popularity')
    plt.title(f'Popularity vs {feature}')
    plt.show()

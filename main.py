import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s_data=pd.read_csv("Spotify_data.csv")

# delete redundant column
s_data.drop(columns=['Unnamed: 0'], inplace=True)

# print all the column names
'''
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
s_data.show()
'''

features=['Energy', 'Valence', 'Danceability', 'Loudness', 'Acousticness']

# make scatterplots for few sample features
'''
for feature in features:
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=s_data, x=feature, y='Popularity')
    plt.title(f'Popularity vs {feature}')
    plt.show()
'''

# let's see correlation between all the features

# extract columns having only numeric values
numeric_columns=s_data.select_dtypes(include=['float64', 'int64']).columns
# extract data for all records only for the above columns
numeric_data=s_data[numeric_columns]

#create correlation matrix
corr_matrix=numeric_data.corr()

# create heatmap
'''
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
'''

# let's have a look at distribution of sample features
'''
for feature in features:
    plt.figure(figsize=(8,5))
    sns.histplot(s_data[feature], kde=True)
    plt.title(f'(Distribution of {feature})')
    plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

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

# time to make a ML model tp predict Popularity for future tracks

# select the features and the target variable
features2=['Energy', 'Valence', 'Danceability', 'Loudness', 'Acousticness', 'Tempo', 'Speechiness', 'Liveness']

x=s_data[features2]
y=s_data['Popularity']

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=42)

# feature normalization
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

# define parameter grid for Random Forest
param_grid={
    'n_estimators': [50,100,200],
    'max_features': ['aoto', 'sqrt', 'log2'],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2,5,10],
    'min_samples_leaf': [1,2,4]
}

grid_search_rf=GridSearchCV(RandomForestRegressor(random_state=42), param_grid, refit=True, verbose=2, cv=5)
grid_search_rf.fit(x_train_scaled, y_train)
best_params_rf=grid_search_rf.best_params_
best_rf_model=grid_search_rf.best_estimator_

# make predictions
y_pred_best_rf=best_rf_model.predict(x_test_scaled)

# show actual vs predicted popularity
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred_best_rf, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)
plt.xlabel('Actual Popularity')
plt.ylabel('Predicted Popularity')
plt.title(f'Actual vs Predicted Popularity (Best Random Forest Model)')
plt.show()

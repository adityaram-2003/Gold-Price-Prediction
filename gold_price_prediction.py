import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the gold price data
gold_data = pd.read_csv("https://raw.githubusercontent.com/nakshatra108/Gold-Price-Prediction/main/Gold%20Price%20Prediction/gld_price_data.csv")

# Drop the 'Date' column
gold_data.drop('Date', axis=1, inplace=True)

# Data Pre-Processing
correlation = gold_data.corr()

plt.figure(figsize=(8, 8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Greens')

# Use displot instead of distplot
sns.displot(gold_data['GLD'], color='red', kde=True)

# Feature Splitting
X = gold_data.drop('GLD', axis=1)
Y = gold_data['GLD']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Machine Learning Model: RANDOM FOREST REGRESSOR
regressor = RandomForestRegressor(n_estimators=100)
# Training the model
regressor.fit(X_train, Y_train)

# Testing the Model
gold_price_predictor = regressor.predict(X_test)

# Validating Original values vs Predicted values
plt.plot(Y_test, color='blue', label='Actual Value')
plt.plot(gold_price_predictor, color='yellow', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()

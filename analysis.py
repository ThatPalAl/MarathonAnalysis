import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('./cleaned_polmaraton_results.csv')

df['Czas_minutes'] = pd.to_timedelta(df['Czas']).dt.total_seconds() / 60
# Two basic features, which I will use for the analysis

X = df[['Wiek']]  
y = df['Czas_minutes']  

#trainig and testing data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#training the model:
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


#lets see the result of the prediction:
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', alpha=0.5, label='training data')
plt.plot(X_test, y_pred, color='red', label='regression line')
plt.title('Age vs race - Linear Regression')
plt.xlabel('Age')
plt.ylabel('Time (min)')
plt.legend()
plt.grid(True)
plt.show()

slope = model.coef_[0]
intercept = model.intercept_

print(f"Slope : {slope}")
print(f"intercept: {intercept}")

residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True, color='purple')
plt.title('distribution of Residuals')
plt.xlabel('actual time')
plt.ylabel('frequency')
plt.grid(True)
plt.show()

#mean squared error:
mse = mean_squared_error(y_test, y_pred)
print(f"MSE : {mse}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.title('predicted vs actual time (in min)')
plt.xlabel('Actual time')
plt.ylabel('predicted time (min)')
plt.grid(True)
plt.show()
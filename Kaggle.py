import pandas as pd
from sklearn.tree import DecisionTreeRegressor
melbourne_file_path = 'E:\Document_Python\csv\melb_data_cost_price.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
#print(melbourne_data.columns)
#dropna giúp hạn chế các feature bị thiếu.
melbourne_data = melbourne_data.dropna(axis=0)
melbourne_feature =['Bathroom','Car','Landsize','Rooms']
X = melbourne_data[melbourne_feature]
# predict
y = melbourne_data.Price
# print(X.describe())
# print(X.head())
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
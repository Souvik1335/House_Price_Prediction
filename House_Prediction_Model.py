from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')

#Load the Dataset
df = pd.read_csv(r'C:\Users\souvi\Videos\AII SUBJECT\HOUSE_GG_COLAB\house_price_1k.csv')
print(df.isnull().sum())

#Define the X & Y
x = df.drop('Price', axis=1)
y = df['Price']

#Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

#Model Creation with Pipeline
pipe = Pipeline([
    ('model', RandomForestRegressor(random_state=42))
])

#Model Train
pipe.fit(x_train, y_train)

#Model Prediction
Model_Prediction = pipe.predict(x_test)

#Model Metrics Evolution
print("Model's r2_score is :- ", r2_score(y_test, Model_Prediction))
print("Model's Mean Absolute Error S is :- ", mean_absolute_error(y_test, Model_Prediction))
print("Model's Mean Squared Error is :- ", mean_squared_error(y_test, Model_Prediction))

#Save as a Pickle model
joblib.dump(pipe, "house_price_model.pkl")
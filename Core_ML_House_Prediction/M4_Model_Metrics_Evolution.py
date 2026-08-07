from M3_Model_Training import model
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from M3_Model_Training import X_test, y_test

# Model Predectin
Model_Prediction = model.predict(X_test)

# Model's r2_score
print("Model's r2_score is :- ", r2_score(y_test, Model_Prediction))

#Model's mean_absolute_error(MAE)
print("Model's mean_absolute_error(MAE) :- ", mean_absolute_error(y_test, Model_Prediction))

# Model's mean_squared_error(MSE)
print("Model's mean_squared_error(MSE) :- ", mean_squared_error(y_test, Model_Prediction))
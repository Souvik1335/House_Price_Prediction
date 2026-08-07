from M2_Feature_Engineering import df, X, y
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Split the Data for Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create the Model
model = RandomForestRegressor(random_state=42)

# Train the Model
model.fit(X_train, y_train)
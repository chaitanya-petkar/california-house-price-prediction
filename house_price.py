import joblib  # It Helps to save trained ML Models and load them back for future use without retraining
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)

X = housing.data  # Features
y = housing.target  # Target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)  # training the model

predictions = model.predict(X_test)  # for prediction
score = model.score(
    X_test, y_test
)  # Compares Real answers Vs Model answers and gives a score

mae = mean_absolute_error(
    y_test, predictions
)  # Checking how far wrong the model is on average

mse = mean_squared_error(y_test, predictions)  # It squares the mistakes
rmse = mse**0.5  # It averages the mistakes and brings back to the orignal vallue


joblib.dump(model, "model.pkl")  # This SAVES Our Trained Model into "model.pkl" file
joblib.dump(scaler, "scaler.pkl")  # This SAVES Our scaler into "scaler.pkl" file


loaded_model = joblib.load("model.pkl")  # This LOADS our trained model from "model.pkl"


new_house = [
    [8.3, 25, 6.2, 1.0, 500, 2.5, 37.8, -122.2]
]  # New House data for Prediction
new_house_scaled = scaler.transform(new_house)  # Scaling the New House Data
prediction = loaded_model.predict(
    new_house_scaled
)  #  Making Prediction Using the Loaded Model


print(housing.data.shape)
print(housing.feature_names)

print(df.head())

print("Missing values:\n", df.isnull().sum())

print("X shape :", X.shape)
print("y shape :", y.shape)

print("Model score:", score)

print("Predicted : ", predictions[:5])
print("Real : ", y_test[:5])

print("Mean Absolute Error : ", mae)

print("MSE : ", mse)
print("RMSE : ", rmse)

print("Model Saved Successfully!")

print("Predicted Price for New House: ", prediction)

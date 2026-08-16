import joblib

model = joblib.load("model.pkl")  # This loads our trained "model.pkl" file
scaler = joblib.load("scaler.pkl")  # This loads our "scaler.pkl" file

new_house = [[4.5, 20, 5.0, 1.0, 1000, 3.0, 34.0, -118.0]]  # New house data

new_house_scaled = scaler.transform(new_house)  # Scaling the New House Data

prediction = model.predict(new_house_scaled)  # Making Prediction Using the loaded model

print("Predicted Price for the new house: ", prediction)  # Printing the Predicted Price

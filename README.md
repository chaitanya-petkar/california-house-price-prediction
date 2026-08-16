# 🏠 California House Price Prediction


<p align="center">
  <b>A Machine Learning project that predicts California house prices using Linear Regression and Scikit-learn.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-orange" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
</p>

---

## 📌 About the Project

**California House Price Prediction** is a beginner-friendly Machine Learning project built using **Python** and **Scikit-learn**.

The project trains a **Linear Regression** model on a California house price dataset and uses the trained model to predict the price of a new house based on its features.

This project demonstrates the complete basic Machine Learning workflow — from loading and preparing data to training, saving, and using a Machine Learning model.

---

## 🎯 Project Objectives

- Understand the basic Machine Learning workflow
- Load and prepare a dataset
- Separate input features and target values
- Scale numerical features
- Train a Linear Regression model
- Save the trained model
- Save the feature scaler
- Load the saved model for prediction
- Generate predictions for new house data

---

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Preparation
   ↓
Feature & Target Separation
   ↓
Feature Scaling
   ↓
Linear Regression
   ↓
Model Training
   ↓
Save Model + Scaler
   ↓
New House Data
   ↓
Prediction
```
---

## 🛠️ Technologies Used
Technology	Purpose
🐍 Python	Programming language
🐼 Pandas	Data handling
🔢 NumPy	Numerical operations
🤖 Scikit-learn	Machine Learning
💾 Joblib	Saving and loading the model

---

## 📂 Project Structure
```text
california-house-price-prediction/
│
├── 📄 house_price.py
├── 📄 house_price.txt
├── 📄 predict.py
├── 📦 model.pkl
├── 📦 scaler.pkl
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📖 README.md
```

---


## 📄 File Description
house_price.py

Contains the main Machine Learning workflow:

- Loads the dataset
- Prepares the data
- Scales the features
- Trains the Linear Regression model
- Saves the trained model
- Saves the scaler

---

```text
predict.py
```
Loads the saved model and scaler and uses them to predict the price of a new house.

```text
house_price.txt
```
Contains the house price dataset used for training the model.

```text
model.pkl
```
Saved trained Linear Regression model.

```text
scaler.pkl
```
Saved feature scaler used to transform input data before prediction.

```text
requirements.txt
```
Contains the Python libraries required to run the project.

---

## 📦 Installation
1. Clone the repository
```text
git clone https://github.com/chaitanya-petkar/california-house-price-prediction.git
```

2. Open the project folder
 ```text
cd california-house-price-prediction
```

3. Create a virtual environment
```text
python -m venv ml-env
```

4. Activate the virtual environment
Windows:
```text
ml-env\Scripts\activate
```

5. Install dependencies
```text
pip install -r requirements.txt
```
---

## ▶️ How to Run
Step 1 — Train the Model
```text
python house_price.py
```

This trains the Linear Regression model and creates:

```text
model.pkl
scaler.pkl
```

Step 2 — Make a Prediction
```text
python predict.py
```
The program loads the trained model and predicts the price for the provided house features.

---

## 📊 Example Prediction

Example output:
```text
Predicted Price for the new house: [2.24877128]
```
The prediction value depends on the input features and the dataset used for training.

---

## 🔬 Machine Learning Model

This project uses:

Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this project, the model learns the relationship between house features and house prices.

The basic idea can be represented as:

```text
Price = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ
```

Where:
```text
Price = predicted house price
X₁ ... Xₙ = house features
β₀ = intercept
β₁ ... βₙ = learned coefficients
```
---

## 📈 Feature Scaling

Before training and prediction, numerical features are scaled using Scikit-learn's feature scaling technique.

The scaler is saved as:
```text
scaler.pkl
```
This ensures that new input data is transformed consistently with the data used during model training.

---

## 🧪 Example Workflow
```text
# Load model
model = joblib.load("model.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")

# Transform new data
new_data_scaled = scaler.transform(new_data)

# Make prediction
prediction = model.predict(new_data_scaled)
```

---

## 🎓 What I Learned

Through this project, I learned the fundamentals of:

- Python for Machine Learning
- Dataset handling
- Feature engineering basics
- Feature scaling
- Supervised Learning
- Linear Regression
- Model training
- Model persistence
- Making predictions with a trained model
- Using Scikit-learn
- Managing Python dependencies

---

## 🚀 Future Improvements

Possible improvements for this project include:

- Add a larger and cleaner dataset
- Add train/test splitting
- Evaluate the model using MAE, MSE and R²
- Compare multiple Machine Learning algorithms
- Build a web interface for predictions
- Deploy the model as an API
- Add data visualization
- Improve prediction accuracy

---

## 📌 Project Status

✅ Completed — Basic Machine Learning House Price Prediction

This project was created as part of my Machine Learning learning journey.

---

## 👨‍💻 Author
## Chaitanya Petkar

Aspiring Software Developer & Machine Learning Enthusiast

## 📌 GitHub:
https://github.com/chaitanya-petkar

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐.

<p align="center"> 
<b>Built with 🐍 Python + 🤖 Machine Learning</b> </p>

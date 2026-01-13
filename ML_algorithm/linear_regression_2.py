import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# -----------------------------
# 1. Create sample dataset
# -----------------------------
data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 5],
    "age": [5, 10, 8, 15, 20],
    "price": [50, 70, 90, 110, 150]  # output
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Split input and output
# -----------------------------
X = df[["area", "bedrooms", "age"]]   # multiple features
y = df["price"]                       # target

# -----------------------------
# 3. Create & train the model
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# 4. Print model parameters
# -----------------------------
print("Coefficients (m values):", model.coef_)
print("Intercept (b value):", model.intercept_)

# -----------------------------
# 5. Make a prediction
# -----------------------------
new_house = pd.DataFrame(
    [[2200, 3, 12]],
    columns=["area", "bedrooms", "age"]
)

predicted_price = model.predict(new_house)
print("Predicted Price:", predicted_price[0])
# Alternatively, using numpy array for prediction:
new_house = np.array([[2200, 3, 12]])  
predicted_price = model.predict(new_house)

print("Predicted Price:", predicted_price[0])  #0 for first element

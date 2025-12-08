# =======================================================
# 🚗 CAR PRICE PREDICTION — FULL MULTIPLE REGRESSION CODE
# =======================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# ------------------------------------
# 1. Create a sample dataset
# ------------------------------------
data = {
    "year": [2015, 2012, 2018, 2010, 2016, 2019, 2014, 2011],
    "mileage": [50000, 70000, 30000, 90000, 40000, 20000, 65000, 80000],
    "engine_cc": [1200, 1300, 1000, 1500, 1400, 1000, 1200, 1300],
    "car_price": [500000, 350000, 650000, 250000, 550000, 700000, 400000, 300000]
}

df = pd.DataFrame(data)

print("🔹 Dataset:\n", df, "\n")

# ------------------------------------
# 2. Split into Input & Output
# ------------------------------------
X = df[["year", "mileage", "engine_cc"]]   # features
y = df["car_price"]                        # target

# ------------------------------------
# 3. Train-Test Split
# ------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ------------------------------------
# 4. Create & Train Model
# ------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------
# 5. Model Parameters
# ------------------------------------
print("🔹 Coefficients (m values):", model.coef_)
print("🔹 Intercept (b value):", model.intercept_, "\n")

# ------------------------------------
# 6. Predict on Test Data
# ------------------------------------
y_pred = model.predict(X_test)

print("🔹 Actual Prices :", list(y_test))
print("🔹 Predicted Prices :", list(y_pred), "\n")

# ------------------------------------
# 7. Model Evaluation
# ------------------------------------
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("📈 R² Score:", r2)
print("📉 Mean Squared Error:", mse, "\n")

# ------------------------------------
# 8. Make a new prediction
# ------------------------------------
# new_car = np.array([[2017, 45000, 1200]])  # Year, Mileage, Engine CC

# ------------------------------------
# alternative way to display the prediction
# ------------------------------------
new_car = pd.DataFrame({
    "year": [2017],
    "mileage": [45000],
    "engine_cc": [1200]
})
predicted_price = model.predict(new_car)

model.predict(new_car)


print("🚗 Predicted Price for New Car:", predicted_price[0])

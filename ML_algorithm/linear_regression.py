import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[1], [2], [3], [4], [5]])  # hours
y = np.array([40, 50, 60, 70, 80])      # marks

# Model
model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for 7 hours:", model.predict([[7]]))

# -----------------------------
# With Train-Test Split and Accuracy
# -----------------------------

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# -----------------------------
# 1. Data
# -----------------------------
X = np.array([[1], [2], [3], [4], [5]])   # hours studied
y = np.array([40, 50, 60, 70, 80])        # marks

# -----------------------------
# 2. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Model Training
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 4. Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 5. Accuracy (R² Score)
# -----------------------------
accuracy = r2_score(y_test, y_pred)

# -----------------------------
# 6. Outputs
# -----------------------------
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("R² Score (Accuracy):", accuracy)
print("Prediction for 7 hours:", model.predict([[7]]))

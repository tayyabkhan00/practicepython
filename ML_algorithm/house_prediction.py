import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor

# Sample dataset creation

data = {
    "size_sqft": [800, 900, 1000, 1100, 1200, 1300, 1500, 1700],
    "bedrooms": [1, 2, 2, 3, 3, 3, 4, 4],
    "location_score": [3, 4, 5, 6, 6, 7, 8, 9],
    "price_lakh": [40, 45, 50, 60, 65, 70, 85, 100]
}

df = pd.DataFrame(data)

# Feature and target separation

X = df.drop("price_lakh", axis=1)
y = df["price_lakh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("Linear Regression R2:", r2_score(y_test, lr_pred))

# Random Forest Regressor

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("Random Forest R2:", r2_score(y_test, rf_pred))


# XGBoost Regressor

xgb = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)

print("XGBoost R2:", r2_score(y_test, xgb_pred))







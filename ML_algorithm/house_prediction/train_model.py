import os
import pandas as pd
import pickle
import json

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "bengaluru_house_data.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")

os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "house_price_model.pkl")
COLUMNS_PATH = os.path.join(MODEL_DIR, "columns.json")

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------
# Data cleaning
# -----------------------------
df.drop(['area_type', 'availability', 'society', 'balcony'], axis=1, inplace=True)
df.dropna(inplace=True)

df['bhk'] = df['size'].apply(lambda x: int(x.split()[0]))
df.drop('size', axis=1, inplace=True)

def convert_sqft(x):
    tokens = str(x).split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(inplace=True)

if 'price_per_sqft' in df.columns:
    df.drop('price_per_sqft', axis=1, inplace=True)

location_stats = df['location'].value_counts()
df['location'] = df['location'].apply(
    lambda x: 'other' if location_stats[x] <= 10 else x
)

dummies = pd.get_dummies(df['location'], drop_first=True)
df = pd.concat([df.drop('location', axis=1), dummies], axis=1)

# -----------------------------
# Train / Test
# -----------------------------
X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Models
# -----------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)
print("Linear Regression R2:", lr.score(X_test, y_test))

xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    random_state=42,
    tree_method="hist",   # CPU-safe
    predictor="cpu_predictor"
)

xgb.fit(X_train, y_train)
print("XGBoost R2:", xgb.score(X_test, y_test))

# -----------------------------
# Save model + columns
# -----------------------------
with open(MODEL_PATH, "wb") as f:
    pickle.dump(xgb, f)

with open(COLUMNS_PATH, "w") as f:
    json.dump(list(X.columns), f)

print("✅ Model and columns saved successfully")

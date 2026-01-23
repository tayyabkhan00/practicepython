import pandas as pd

df = pd.read_csv("/Users/tayyabkhan/python/ML_algorithm/house_prediction/data/bengaluru_house_data.csv")
df.head()


df.drop(['area_type','availability','society','balcony'], axis=1, inplace=True)


df = df.dropna()


df['bhk'] = df['size'].apply(lambda x: int(x.split()[0]))
df.drop('size', axis=1, inplace=True)


def convert_sqft(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df = df.dropna()



df['price_per_sqft'] = df['price']*100000 / df['total_sqft']


location_stats = df['location'].value_counts()
df['location'] = df['location'].apply(
    lambda x: 'other' if location_stats[x] <= 10 else x
)


dummies = pd.get_dummies(df['location'], drop_first=True)
df = pd.concat([df.drop('location', axis=1), dummies], axis=1)


from sklearn.model_selection import train_test_split

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

print("Linear Regression R2:", lr.score(X_test, y_test))


from xgboost import XGBRegressor

xgb = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

xgb.fit(X_train, y_train)

print("XGBoost R2:", xgb.score(X_test, y_test))


import pickle
import json

pickle.dump(xgb, open("model/house_price_model.pkl", "wb"))

with open("model/columns.json", "w") as f:
    json.dump(X.columns.tolist(), f)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data
X = [[25], [30], [35], [40], [45]]
y = [0, 0, 1, 1, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(model.predict([[28]]))

# ---------------------without train-test split---------------------
from sklearn.ensemble import RandomForestClassifier

# age
X = [[22], [25], [47], [52], [46], [56]]

# buys product? (0 = No, 1 = Yes)
y = [0, 0, 1, 1, 1, 1]

model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

print(model.predict([[30]]))  # younger person
print(model.predict([[50]]))  # older person

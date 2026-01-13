from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6]]   # hours
y = [0, 0, 0, 1, 1, 1]              # pass/fail

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[3.5]]))       # 0 or 1
print(model.predict_proba([[3.5]])) # probability

# output:
# 0.49996763 → probability of class 0 (NO)
# 0.50003237 → probability of class 1 (YES)

# Complete example with train-test split and accuracy evaluation
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data
X = [[10], [20], [30], [40], [50]]
y = [0, 0, 0, 1, 1]   # 0 = No, 1 = Yes

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

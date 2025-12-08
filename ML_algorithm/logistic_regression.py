from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6]]   # hours
y = [0, 0, 0, 1, 1, 1]              # pass/fail

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[3.5]]))       # 0 or 1
print(model.predict_proba([[3.5]])) # probability

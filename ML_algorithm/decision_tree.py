from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[22], [25], [47], [52], [46], [56]]     # age
y = [0, 0, 1, 1, 1, 1]                       # buys product? yes/no

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[30]]))
print(model.predict([[50]]))
'''
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plot_tree(model, filled=True)
plt.show()
'''
from sklearn.tree import DecisionTreeClassifier

X = [
    [22, 20000, 0, 400, 1],
    [25, 50000, 0, 650, 1],
    [47, 80000, 0, 700, 0],
    [52, 60000, 1, 720, 0],
    [46, 30000, 1, 450, 1]
]

# buy product? (0 = No, 1 = Yes)
y = [0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

# new customer
print(model.predict([[30, 40000, 1, 600, 1]]))



from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data
X = [[25], [30], [35], [40], [45]]
y = [0, 0, 1, 1, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

print("Accuracy:", rf.score(X_test, y_test))

# Top 3 important features
importances = rf.feature_importances_
top3 = sorted(zip(importances, iris.feature_names), reverse=True)[:3]
print("Top 3 important features:", top3)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Sample data
X = [[25], [30], [35], [40], [45]]
y = [0, 0, 1, 1, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Example usage

from sklearn.neighbors import KNeighborsClassifier

X = [[40], [45], [50], [70], [75], [80]]  # marks
y = ['A', 'A', 'A', 'B', 'B', 'B']

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print(model.predict([[55]]))



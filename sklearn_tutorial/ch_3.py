from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

print("Test X:", X_test)
print("Predictions:", pred)






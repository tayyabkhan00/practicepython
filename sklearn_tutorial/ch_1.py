from sklearn.tree import DecisionTreeClassifier

# 1. Data
X = [[140], [150], [160], [170]]  # heights
y = [0, 0, 1, 1]  # 0 = short, 1 = tall

# 2. Create model
model = DecisionTreeClassifier()

# 3. Train model
model.fit(X, y)

# 4. Predict
print(model.predict([[155]]))


# fit() = teach the model
# predict() = ask the model
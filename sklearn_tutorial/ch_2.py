from sklearn.model_selection import train_test_split

X = [[1],[2],[3],[4]]   # features
y = [2,4,6,8]           # targets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1, random_state=0
)

print("Train X:", X_train)
print("Test X:", X_test)


# test_size=0.25 → 25% test, 75% train
# random_state=0 → makes split same every time

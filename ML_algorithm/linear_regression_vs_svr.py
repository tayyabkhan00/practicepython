from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

X = [[1], [2], [3], [4], [5]]
y = [3, 4, 5, 6, 20]

# Linear Regression
lr = LinearRegression()
lr.fit(X, y)

# SVR
svr = SVR(kernel='linear',C=1, epsilon=0.5)

svr.fit(X, y)

print("LR prediction (2.5):", lr.predict([[2.5]]))
print("SVR prediction (2.5):", svr.predict([[2.5]]))

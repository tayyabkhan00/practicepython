# 1. basic implementation of two sum problem
'''arr = [2, 7, 11, 15]   # array
target = 9             # value to find

for i in range(len(arr)):       # pick first number
    for j in range(i+1, len(arr)):   # pick second number
        if arr[i] + arr[j] == target:
            print("Indices:", i, j)
'''
# 2. beginner_methods to take input from user and print output
arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)

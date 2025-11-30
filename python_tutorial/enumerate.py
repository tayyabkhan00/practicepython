fruits = ["apple", "banana", "mango"]

for index, item in enumerate(fruits):
    print(index, item)

fruits = ["apple", "banana", "mango"]

# Starting index from 1
for index, item in enumerate(fruits, start=1):
    print(index, item)

nums = [10, 20, 30]

# Printing index and value of each element using enumerate
for i, n in enumerate(nums):
    print("Position:", i, "| Value:", n)

nums = [5, 10, 15]

# Doubling each element in the list using enumerate
for i, n in enumerate(nums):
    nums[i] = n * 2

print(nums)


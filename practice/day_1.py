import pandas as pd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 1. Create a new list of squares of only EVEN numbers
squares=[]
for i in numbers:
    if i%2==0:
      squares.append(i*i)
print(squares)

squares=[i*i for i in numbers if i%2==0]
print(squares)

# 2. Create a dictionary: number → "even" or "odd"

dict={
   i:"even" if i%2==0 else "odd" for i in numbers
}
print(dict)


# 3. Write a function that returns:
#    - "small" if number < 5
#    - "medium" if 5–7
#    - "large" if > 7
def fun(n):
   return "small" if n<5 else "large" if n>7 else "medium"
print(fun(2))
print(fun(1))
print(fun(7))
print(fun(9))
numbers = [1,2,3,4,5,6,7,8,9]

labels = [fun(i) for i in numbers]
print(labels)


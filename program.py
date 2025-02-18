
""""
hi 

print(5)
print("hey im a \"good boy\"")
print("hey",6,7,sep="~",end="009\n")
print("tayyab")
a=1
b="tayyab"
c=True
d=None
print(a)
print(b)
print(c)
print(d)
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of d is",type(d))
list =[7,8,3,[-4,5],"apple","banana"]
print(list)
tuple=("parrot","sparrow","crow")
print(tuple)
dict={"name":"tayyab","age":22,"canvote":True}
print(dict)
# END OF L6
name="tayyab"
course="btech ai and data science"
print("hello" + name,course) 
print(name[0])
for charachter in name:
    print(charachter)
# END OF L11
print(len(name))    
print(name[0:6])
print(name[-4:-1])
"""
# a="tayyab!! !"
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("tayyab","paak"))
# print(a.split(" "))
# # END OF L13
# a=int(input("enter your age"))
# print("you're age is:",a)
# if(a>18):
#     print("you're applicalble for driving")
# else:
#     print("you're not applicable for driving")
# x=int(input("enter the value of x: "))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case _:
#         print("x")   
# name="tayyab"
# for i in name:
#     print(i) 
# for i in range(10):
#     print(i)
# end of l17
# for i in range(12):
#     if(i==10):
#         print("skip the iteration")
#         continue
#     print("5x",i,"=",5*i)
# def division(a,b):
#     divide=a/b
#     print(divide)
# a=int(input("enter the digit"))
# b=int(input("enter the second digit"))
# division(a,b)
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
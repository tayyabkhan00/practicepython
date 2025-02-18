print("calculator")
a=int(input("enter the first digit: "))
b=int(input("enter the second digit: "))
print("select operator: ")
print("add +")
print("subtract -")
print("multiplication *")
print("divide /")
operation=input("enter operation: ")
if operation=='+':
    result=a+b
    print("result:",result)
elif operation=='-':
    result=a-b
    print("result",result)
elif operation=='*':
    result=a*b
    print("result",result)
elif operation=='/':
    result=a/b
    print("result",result)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"the salary of {self.name} is {self.salary}")
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
e1=Employee("rohan",12000)
e2="john-10000"
e2=Employee.fromStr(e2)
print(e2.name)
print(e2.salary)
# print(e1.name)
# print(e1.salary)
class Employee:
    def __init__(self,id,name):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the name of employee:{self.name}is{self.id}")
class Programmer(Employee):
    def showlanguage(self):
        print("the language is default")
e1=Employee("rohan",10)
e1.showdetails()
e2=Programmer("rehan",20)
e2.showdetails()
e2.showlanguage()

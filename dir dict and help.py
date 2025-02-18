class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
e1=Person("rohan",2)
print(e1.__dict__)
print(e1.__dir__)
print(help(Person))
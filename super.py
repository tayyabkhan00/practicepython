class Parent:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print(f"the id of {self.name} is {self.id}")
class Child(Parent):
    def __init__(self,name,id,center):
        super().__init__(name,id)
        self.center=center

a=Parent("cambridge","245")
b=Child("harward","450","567")
print(a.name)
print(a.id)
print(b.name)
print(b.id)
print(b.center)
# what is the role of __init__ function()?
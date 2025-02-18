class Avengers:
    def __init__(self,name,members):
        self.name=name
        self.members=members
    def showdetails(self):
       print(f"name:{self.name}")
       print(f"members:{self.members}")
class Revengers(Avengers):
    def __init__(self,name,planet):
        Avengers.__init__(self,name,members="5")
        self.planet=planet
    def showdetails(self):
        Avengers.showdetails(self)
        print(f"planet:{self.planet}")
class Guardians(Revengers):
    def __init__(self,name,place):
        Revengers.__init__(self,name,planet="asgard") 
        self.place=place
    def showdetails(self):
        Revengers.showdetails(self)
        print(f"place:{self.place}")
a=Guardians("thor","galaxy")
a.showdetails()
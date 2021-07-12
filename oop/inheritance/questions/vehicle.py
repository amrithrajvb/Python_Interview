#create a child class bus that will inherit all of the vehicle and methods of vehicle class
class Vehicle:
    def __init__(self,milage,color,company):#def setvalue(self,milage,color,company)
        self.milage=milage
        self.color=color
        self.company=company

class Bus(Vehicle):
    def printvalue(self):
        print("milage:",self.milage)
        print("color:", self.color)
        print("name:", self.company)
obj=Bus(60,"black","maruti")
#obj.setvalue(60,"black","maruti")
obj.printvalue()


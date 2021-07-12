class Vehicle:
    def setValue(self,model,color,milage):
        self.model=model
        self.color=color
        self.milage=milage
class Car(Vehicle):
    def printValue(self):
        print("model:",self.model)
        print("color :",self.color)
        print("milage",self.milage)
c=Car()
a=input("please enter the model")
b=input("please enter the color")
d=input("please enter the milage")
c.setValue(a,b,d)
c.printValue()


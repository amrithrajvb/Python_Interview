#oop
#class: design pattern/blueprint
#object: real world entity
#reference: to perform operations on object(providing memory location)

class Person:
    def walk(self):#instance keyword-self mainly usedfor method is identifying inside the class
        print("walking")
    def talk(self):
        print("talking")
obj=Person()
obj.walk()
obj.talk()
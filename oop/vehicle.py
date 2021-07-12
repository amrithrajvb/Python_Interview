class Vehicle:
    def printvalue(self,model,color,regno,company):
        self.model=model
        self.color=color
        self.regno=regno
        self.company=company
    def print(self):
        print("model",self.model)
        print("color",self.color)
        print("regno",self.regno)
        print("company",self.company)
    def __str__(self):
        return self.model

v=Vehicle()
v.printvalue("101a","black","kl133060","honda")
v.print()
print(v)

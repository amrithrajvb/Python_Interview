#polymorphism--many forms name as same
#over loading--doesn't support
#over riding

class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Display(Operators):
    def num(self,n3):
        self.n3 = n3
        print(self.n3)
d=Display()
d.num(1)
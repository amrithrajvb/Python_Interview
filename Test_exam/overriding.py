class Book:
    def pvalue(self,publish_name,pages):
        self.publish_name=publish_name
        self.pages=pages
        print("publish name", self.publish_name, "pages", self.pages)

class Computer(Book):
    def pvalue(self,clas,schl):
        self.clas=clas
        print("child method",self.clas)

c=Computer()
m=input("please enter this text for")
c.pvalue(m,"fdfd")
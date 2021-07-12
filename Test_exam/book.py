class Book:
    Library_name="DC name"
    def Bvalue(self,book_name,author,pages):

        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printValue(self):
        print("Library_Name:",Book.Library_name)
        print("book name:",self.book_name)
        print("author :",self.author)
        print("no of pages:",self.pages)

b=Book()
a=input("please enter the Library name")
c=input("please enter the book name")
d=input("please enter the author")
e=int(input("please enter the no of pages"))
b.Bvalue(c,d,e)
b.printValue()

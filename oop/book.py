# class Book:
#     def inputing(self,book_name,author,pages,Library_name):
#         self.book_name=book_name
#         self.author=author
#         self.page=pages
#         self.Library_name=Library_name
#         print("book name:",self.book_name,"\nauthor is:",self.author,"\npage count:",self.page,"\nLibrary name:",self.Library_name)
# obj=Book()
# a=input("please enter the book name")
# b=input("please enter the authorname")
# c=int(input("please enter the total page number"))
# d=input("please enter the Library_name")
# obj.inputing(a,b,c,d)

# 2 types of variable

#static variable---related to class--access by class name
# instance variable---related to method---access by self

#using statcic method

class Books:
    Library_name="DC books"
    def setVal(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.page=pages
    def printVal(self):
        print("book name:",self.book_name)
        print("author name:",self.author)
        print("pages:",self.page)
        print("Library name",Books.Library_name)
obj1=Books()
a1=input("please enter the book name")
b1=input("please enter the authorname")
c1=int(input("please enter the total page number"))
obj1.setVal(a1,b1,c1)
obj1.printVal()

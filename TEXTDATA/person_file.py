# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def print(self):
#         print("name", self.name)
#         print("age",self.age)
#
#     def __str__(self):
#             return self.name
# f = open("person", 'r')
# # print(f)
# for i in f:
#     words = i.rstrip("\n").split(",")
#     # print(words)
#     name=words[0]
#     age=words[1]
#     obj=Person(name,age)
#     print(obj)
#     obj.print()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printing(self):
#         print("Name is",self.name,"age is",self.age)
# f1=open('person','r')
# for i in f1:
#     words=i.rstrip("\n").split(",")
#     name=words[0]
#     age=words[1]
#     obj=Person(name,age)
#     obj.printing()











            # words = i.split(" ")
            # # words=i.rstrip('\n').split(" ")-rstrip used for removing particular element
            # for j in words:
            #     print(j)
            #     # self.count=j
            #     # print(self.count)
            #     break
import pandas as pd
class Items:
    def __init__(self,InvoiceNo,StockCode,Description,Quantity,InvoiceDate,k,CustomerID,Country):
        self.InvoiceNo=InvoiceNo
        self.StockCode=StockCode
        self.Description=Description
        self.Quantity=Quantity
        self.InvoiceFDate=InvoiceDate
        self.k=k
        self.CustomerID=CustomerID
        self.Country=Country

    def __str__(self):
        return "quantity : "+self.Quantity+"  customer id: "+self.CustomerID+"  invoice date: "+self.InvoiceFDate


lisd=[]
f=open('datas','r')
for i in f:
    words = i.rstrip("\n").split(",")
    InvoiceNo = words[0]
    StockCode= words[1]
    Description=words[2]
    Quantity=words[3]
    InvoiceDate=words[4]
    UnitPrice=words[5]
    CustomerID=words[6]
    Country=words[7]
    # print(int(float(UnitPrice)))
    k=int(float(UnitPrice))
    print(k,"hghgfhfg")
    item=Items(InvoiceNo,StockCode,Description,Quantity,InvoiceDate,k,CustomerID,Country)
    lisd.append(item)


qnty=[]
for j in lisd:
    print(j)
    qnty.append(j.Quantity)
# print(qnty)
for st in lisd:
    if st.Quantity == max(qnty):
        print(max(qnty))
        print(st.CustomerID, st.InvoiceFDate, st.Quantity)
#
#
#
#         -----second
print(lisd)
sec=[]
for m in lisd:
    c=m.Quantity
    d=m.k
    F= int(c)*int(d)
    # for i in F:
    #     i.sort()
    #     print(i)
    print(F)
    print(m.k,"UNI")
    print(m.Quantity,"QN")
    # print(C)
    # df = pd.DataFrame(sec)
    # df_first_3 = df.head(3)
    # for j in df_first_3:
    #     print(df_first_3)
    print(m.InvoiceNo,m.Country,m.CustomerID,m.Description,F)


--THIRD
















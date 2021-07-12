# class Bank:
#     def accoun_Creation(self,name,place,phone):
#         self.name=name
#         self.place=place
#         self.phone=phone
#         print(" name:",name,"\n place:",place,"\n phone",phone)
#     def deposit(self,dep_amount):
#         balace=0
#         self.balance=balace
#         self.dep_amount=dep_amount
#         self.balance=self.dep_amount+self.balance
#         print("your current account balance",self.balance)
#     def withdraw(self,withdraw_amount):
#         self.withdraw_amount=withdraw_amount
#         self.balance=self.balance-self.withdraw_amount
#         print("your current balance",self.balance)
#
# b=Bank()
# n=input("please enter the name")
# c=input("enter the place")
# d=int(input("enter the phone number"))
# b.accoun_Creation(n,c,d)
# e=int(input("enter your deposit amount"))
# b.deposit(e)
# f=int(input("enter the withdrawl amount"))
# b.withdraw(f)



class Bank:
    def seValue(self,name,place,phonenumber):
        self.name=name
        self.place=place
        self.phonenumber=phonenumber
        print("name:",self.name,"\n place:",self.place,"\n phone:",self.phonenumber)
    def deposit(self,deposit_amount):
        balance=0
        self.balance=balance
        self.deposit_amount=deposit_amount
        self.balance=self.deposit_amount+self.balance
        print("your account balance:",self.balance)
    def withdrawal(self,withdrawal_amount):
        self.withdrawal=withdrawal_amount
        self.balance=self.balance-self.withdrawal
        print("current balance",self.balance)
b=Bank()
nm=input("enter your name")
pl=input("enter your place")
ph=input("enter your phone number")
b.seValue(nm,pl,ph)
dep=int(input("please enter the deposit amount"))
b.deposit(dep)
withd=int(input("enter the withdrwal amount"))
b.withdrawal(withd)


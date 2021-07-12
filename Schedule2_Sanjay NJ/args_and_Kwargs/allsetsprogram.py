# lis=[3,5,7,9,34,37]
# lis.sort(reverse=True)#method
# st=sorted(lis)#function
#
# def printPerson(**kwargs):
#     print(kwargs["wlocation"])
# printPerson(wlocation="kakkanad",hlocation="pala")



#bank

class Bank:
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user3", "balance": 6000},
        1004: {"acconu_num": 1004, "password": "user4", "balance": 7000},
        
    }
    session={}
    def validate_account(self,acc_no):
        if acc_no in self.users:
            return True
        else:
            return False

    def authentication(self,**kwargs):
        acc_no=kwargs["acc_no"]
        password=kwargs["password"]
        user=self.validate_account(acc_no)
        if user:
            if (password==self.users[acc_no]["password"]):
                self.session['user']=acc_no
                print("login success")
                return acc_no
            else:
                print("invalid password")
                return -1 # for invalid password
        else:
            print("invalid account number")
            return 0 #invalid account number
    def balance_enquiry(self,acc_no):
        if (acc_no==self.session['user']):
            print(self.users[acc_no]["balance"])
            # balance=self.users[acc_no]["balance"]
            # return balance
        else:
            print("you must login")
    def fund_transfer(self,user,to_acc_no,amount):
        if self.validate_account(to_acc_no):
            balance=self.users[user]["balance"]
            # balance=self.balance_enquiry(user)
            if balance<amount:
                print("insufficient balance")
            else:
                self.users[user]["balance"]-=amount
                self.users[to_acc_no]["balance"]+=amount
    def logout(self):
        self.session["user"]=0

obj=Bank()
user=obj.authentication(acc_no=1000,password="user1")
if (user==-1)|(user==0):
    print("authentication failed")
else:
    obj.balance_enquiry(user)
obj.fund_transfer(user,1002,1000)
obj.balance_enquiry(user)

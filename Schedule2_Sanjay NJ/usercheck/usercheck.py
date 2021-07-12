users={
    1000:{"acconu_num":1000,"password":"user1","balance":3000},
    1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
    1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
    1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
}

#to authenticate user name and password

def authenticate(user,password):
    if user in users:
        if password==users[user]["password"]:
            print("success")
        else:
            print("invalid password")
    else:
        print("invalid account number")
authenticate(1000,"user2")


#get the account balacnce which corresponsing to providing account number

def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account number")
get_balance(1000)







##using **kwargs


def authenticate(**kwargs):
    user=kwargs["accno"]
    password=kwargs["password"]
    if user in users:
        if password==users[user]["password"]:
            print("success")
        else:
            print("invalid password")
    else:
        print("invalid account number")
authenticate(accno=1000,password="user1")


#get the account balacnce which corresponsing to providing account number

def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account number")
get_balance(1000)
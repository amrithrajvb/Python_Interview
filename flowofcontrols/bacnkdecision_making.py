
current_balance=100000
amount=int(input("enter the amount"))
if  current_balance < amount:
    print("insufficient balance")
else:
    print("your balance is", current_balance - amount)


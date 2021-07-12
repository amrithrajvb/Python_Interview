def admin_required(func):
    def wrapper(user,pin):#no of variables should be same
        if user!="admin":
            raise Exception("you are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_account(user,accountno):
    return str(accountno)+"delete"
print(change_pin("admin",1000))
print(delete_account("admin",1000))

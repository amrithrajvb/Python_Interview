import re
n=input("please enter your email id:")

x="[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$"

matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")
import re
f=open("phone","r")
x="[+][9][1]\d{10}$"
for i in f:
    numbers=i.rstrip("\n")
    matches=re.fullmatch(x,numbers)
    if matches is not None:
        print(i)
    

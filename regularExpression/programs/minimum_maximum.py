import re
n=input("enter the elements")
x="[\D]{8,15}"# if we need numbers also[\d][a-zA-z]{8,15}
matcher=re.fullmatch(x,n)
if matcher is not None:
    print("valid")
else:
    print("invalid")
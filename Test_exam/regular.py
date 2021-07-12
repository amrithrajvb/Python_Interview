#starting enad uppercase and limit5,10

# import re
# n=input("enter the elements")
# x="^[A-Z][a-zA-Z0-9]{3,8}[A-Z]$"
# #b='^[A-Z]\W{3,8}[A-Z]$'
# matcher=re.fullmatch(x,n)
# if matcher is not None:
#     print("valid")
# else:
#     print("invalid")



import re
n="Asdsd Bdssdsd Hk hK Jll"
x="[A-Z][a-z]+"
matcher=re.finditer(x,n)
for match in matcher:
    print(match.start())
    print(match.group())



# import re
# n=input("enter the string")
#
# x="^a\d*b$"
# matcher=re.fullmatch(x,n)
# if matcher is not None:
#
#     print("valid")
# else:
#     print("invalid")










import re
n="helloo"#n=""--work in * but not in +
x ='\w*'#* checking the possitions
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
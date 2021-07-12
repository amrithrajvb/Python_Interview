#x="a$" #end with a

import re
x="a$"
r="aaa abc aaaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
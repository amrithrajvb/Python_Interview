# x="a{2,3}" mininimum count maximum count
#first check the maximum

import re
x="a{2,3}"
r="aaa abc aaaaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
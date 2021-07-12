#x="a*" #count including zero number of a

import re
x="a*"#checking if a not in that postion,
r="aaa abc aaaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
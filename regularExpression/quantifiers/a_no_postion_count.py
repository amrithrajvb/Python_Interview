#x="a{4}# no of possition

import re
x="a{3}"
r="aaa abc aaaa cba"#taken the number of times the element present
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
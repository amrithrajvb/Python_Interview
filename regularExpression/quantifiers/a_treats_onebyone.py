#x="a?" count a as each including zero of a
import re
x="a?"# treat as one by one
r="aaa abc aaaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
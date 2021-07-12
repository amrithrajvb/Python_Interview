#x="a+" #a including group
import re
x="a+"#min count 1 ,maxcount not defined
r="aaa abc aaaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())




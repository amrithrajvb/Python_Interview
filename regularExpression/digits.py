# x='[0-9]' check digits

# import re
# x="[0-9]"
# matcher=re.finditer(x,"123abc@kjfkADAS10656847498FSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#checking sybols
import re
x="[^0-9a-zA-Z]"
matcher=re.finditer(x,"123abc@kjfkADAS10656847498FSDdabc")
for match in matcher:
    print(match.start())
    print(match.group())

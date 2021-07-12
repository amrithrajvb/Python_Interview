# import re
# x='[a-z]'
# matcher=re.finditer(x,"abc@kjfkADASFSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#
# import re
# x="[A-Z]"
# matcher=re.finditer(x,"abc@kjfkADASFSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())


#COMPAINE

import re
x="[A-Za-z]"
matcher=re.finditer(x,"abc@kjfkADASFSDdabc")
for match in matcher:
    print(match.start())
    print(match.group())


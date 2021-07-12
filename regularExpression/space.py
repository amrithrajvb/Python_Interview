import re
x="\s"
matcher=re.finditer(x,"ab c@kjfkADA SFSDdabc")
for match in matcher:
    print(match.start())
    print(match.group())

#
x="\d"#take only digits
matcher=re.finditer(x,"ab c@kjfkADA SFSDdabc")
for match in matcher:
    print(match.start())
    print(match.group())

# x="\D"#except digits
# matcher=re.finditer(x,"ab c@kjfkADA SFSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# x="\w"
# matcher=re.finditer(x,"ab c@kjfkADA SFSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# x="\W"
# matcher=re.finditer(x,"ab c@kjfkADA SFSDdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())

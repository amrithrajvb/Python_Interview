# x='[abc]' #either a b or c
import  re
x="[abc]"
matcher=re.finditer(x,"abc @kjfkdabc")
for match in matcher:
    print(match.start())
    print(match.group())

# x='[^abc]'except abc
# import  re
# x='[^abc]'
# matcher=re.finditer(x,"abc@kjfkdabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())
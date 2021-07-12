#pattern matching

# re--package for pattern matching

#only using in strings


import re

count=0
matcher=re.finditer('ab','aaabannnabnhfjfabkkkdfdabkhjkj')
# print(matcher)--#get memory address
for match in matcher:
    count+=1
print("count=",count)
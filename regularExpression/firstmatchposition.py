import re
count=0
matcher=re.finditer('ab','abklfdjsjdslbfdsfbdsabdfdoiabdfjab')
for match in matcher:
    print("match availble at",match.start())#return match possitions
    print("group=",match.group())#which object find match
    count+=1
print("count=",count)
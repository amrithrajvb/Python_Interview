a="athira123kv"
n="1234567890"

print(n)
c=""
d=""
count=0
countn=0
for i in a:
    if i not in n:
        c=c+i
        count=count+1
    elif n not in a:
        d=d+i
        countn=countn+1
print(c,count)
print(d,countn)





##
s="athira123kv"
n="1234567890"
count=0
countn=0
for i in s:
    if i in n:
        countn=countn+1
    else:
        count=count+1
print(count)
print(countn)

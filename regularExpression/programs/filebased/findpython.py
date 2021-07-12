import re
f=open("pythondatascinceBD","r")
f2=open("py2","w")
x="([L][U][M]\d{2}[P][Y]\d{3}$)"
x2="[A-Z]{3}\d{2}[P][Y]\d{3}$"
for i in f:
    words=i.rstrip("\n")
    matcher=re.fullmatch(x2,words)
    if matcher is not None:
        f2.write(words)
        f2.write("\n")
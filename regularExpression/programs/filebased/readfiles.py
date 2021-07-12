# import re
# x=open("registrationNumber","r")
# x2=open("matchesRegister","w")
# n="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"#KL-[K][L]\d{2}[A-Z]{2}\d{4}
# for i in x:
#     words=i.rstrip("\n")
#     # print(words)
#     match=re.fullmatch(n,words)
#     # a=match.group(1)
#     # # print(a)
#     if match is not None:
#         x2.write(match.group())
#         x2.write("\n")

#Luminar

import re
x=open("registrationNumber","r")
x2=open("matchesRegister","w")
n="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"#KL-[K][L]\d{2}[A-Z]{2}\d{4}
for i in x:
    words=i.rstrip("\n")
    # print(words)
    match=re.fullmatch(n,words)
    if match!=None:
        x2.write(i)
        x2.write("\n")

    # for matcher in match:
        # print(matcher.group())
        # if matcher is not None:
        #     x2.write(matcher)
        # else:
        #     print("invalid")





# f1=open("wordcounttext",'r')
# dic={}
# for i in f1:
#     words=i.rstrip("\n").split(" ")
#     #words=i.rstrip('\n').split(" ")-rstrip used for removing particular element
#     for j in words:
#         count=words.count(j)
#         dic.update({j:count})
# print(dic)
#












f1=open("test","r")
dic={}
for i in f1:
    words=i.rstrip("\n").split(",")
    for j in words:
        count=words.count(j)
        dic.update({j:count})
print(dic)

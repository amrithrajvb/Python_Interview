# inp=input("please enter the element")
# b=inp.split(" ")
# dic={}
# count=0
# print(b)
# for i in b:
#     for dic[i] in i:
#         if dic[i]==i:
#             count=count+1
#             #dic[i] = count
#         break
#     dic[i]=count
#
# print(dic)
        # if dic[i] in i:
        #  cont=count+1
        #  dic[i]=count

# #luminar
#
# count={}
# data="hai helo hai"
# words=data.split(" ")
# for word in words:
#     if word not in count:
#         count.update({word:1})
#     else:
#         val=int(count[word])
#         val+=1
#         count.update({word:val})
# print(count)

#count keyword using

str=input("please enter")
words=str.split(" ")
dic={}
for i in words:
    count=words.count(i)
    dic.update({i:count})
print(dic)




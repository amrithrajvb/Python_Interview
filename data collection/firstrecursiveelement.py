am=input("print")
count=0
for i in am:
    count=am.count(i)
    print(count)
    if count > 1:
        break
print("first recursive element is",i)

        #if c==i:



#lumina
p=input("enter")
count={}
for i in p:
    if i not in count:
        count.update({i:1})
    else:
        print("first reverse element",i)
        break
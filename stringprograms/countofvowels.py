# #a="aeikka"
# a=input("enter the string")
# b="aeiou"
# count=0
# for i in a:
#     if i in b: #if i in "aeiou"
#         count=count+1
# if count == 0:
#     print("no vowels")
# else:
#    print(count)
#
#

inp=input("enter the element")
vowels="aeiou"
count=0
for i in inp:
    if i in vowels:
        print(i)
        count=count+1
if count==0:
    print("no vowels")
print(count)
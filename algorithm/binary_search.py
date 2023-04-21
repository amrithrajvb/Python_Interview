#binary search
#first sort the list and set a middle element and compred
# the element which we trying find , then mid >/< finding elemment then proceed the remaining portion whichis
#satisfy the mid ><finding element

#linearsearch
#search my each element
# a=[3,5,7,2,9,23,4,6,3,71,22,8,42,10]
# inp=int(input("please enter the search element"))
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# mid=len(a)//2
# #cap=a[mid]
# print(mid)
# #print(cap)
# if inp > mid:
#     for k in range(mid,-1):
#         print("elemet present in second")
#         #print()
# else:
#     for v in range(0,mid):
#         print("present in first")
#
#
#
#
#
# #a.sort()
# #print(a)
#

#luminar program
lst=[6, 32, 3, 1]
def bsearch():
    lst.sort()
    print(lst)
    inp=int(input("enter the element"))
    flag=0 #if the element is present change the value
    low=0
    upp=len(lst)-1 # to take last element also based on index
    while low <= upp:
        mid=(low +upp) // 2
        print(mid)
        if inp >lst[mid]:
            low=mid+1#changed mid value also changed
        elif inp < lst[mid]:
            upp=mid -1
        elif inp == lst[mid]:
            flag=1
            break
    if flag==1:
        print(mid,"found")#for possition
    else:
        print("not found")
bsearch()

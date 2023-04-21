# import random
#
# for i in range(10):
#     t=random.randint(1,1000)
#     print(t)
#
#
#
# a=['e','rt','t','f']
# c={}
# price=1
# for i in a:
#     c[i]=price
#     price+=1
# print(c)
# for name,p in c.items():
#     print(name,":",p)
# #
# #
# import datetime
# import shutil
# import time
#
# #
# # def k(arr,N):
# #     sum=0
# #     a={}
# #     for i in range(N):
# #         if arr[i] in a:
# #             a[arr[i]] +=1
# #         else:
# #
# #             a[arr[i]]=1
# #     print(a)
# #
# #     for key,value in a.items():
# #         if(value % 2 ==0):
# #             sum += key
# #     return sum
# #
# #
# # arr=[1,2,2,5,1,5]
# # N=len(arr)
# # print(k(arr,N))
#
# def searchs(arr,N):
#     sum=0
#     a={}
#     for i in range(N):
#         if arr[i] in a:
#             a[arr[i]] +=1
#         else:
#             a[arr[i]]=1
#     print(a)
#
#     for key,value in a.items():
#         if(value%2==0):
#             sum +=key
#     return sum
#
# arr=[12,83,6,6,23,70,83]
# N=len(arr)
# print(searchs(arr,N))
#
# #calendar
#
# import calendar
#
#
# cal=calendar.TextCalendar(calendar.SUNDAY)
# ft=cal.formatmonth(2022,2)
#
# print(ft)
#
#
# ##os
#
# import os
# from os import path
# #
# # print(os.name)
# #
# # # print("exist"+ str(path.exists("person.txt")))
# # # print("file" + str(path.isfile("person.txt")))
# # # print("file" + str(path.isdir("person.txt")))
# #
# #
# # print("file" + str(path.realpath("person.txt")))
# # print("file" + str(path.split(path.realpath("person.txt"))))
# #
# #
# # a=time.ctime(path.getmtime("person.txt"))
# # print(a)
# # print(datetime.datetime.fromtimestamp(path.getmtime("person.txt")))
#
#
# ##shallo copy
# #
# # if path.exists("person.txt"):
# #     src=path.realpath("person.txt")
# #     dst=src+".bak"
# #     shutil.copy(src,dst)
# #     shutil.copystat(src,dst) ##moremodifiction details
# #
# #
# # os.rename("person.txt","emp.txt")
# #
#
# ##make zip
#
# from shutil import make_archive
#
# src = path.realpath("emp.txt")
#
# root_dir,tail=path.split(src)
# shutil.make_archive("last_archive","zip",root_dir)


def searchs(arr,N):
    sum=0
    a={}
    for i in range(N):
        if arr[i] in a:
            a[arr[i]]+=1
        else:
            a[arr[i]]=1
    print(a)
    for key,value in a.items():
        if (value%2==0):
            sum+=key
    return sum

arr=[12,83,6,6,23,70,83]
len=len(arr)
print(searchs(arr,len))
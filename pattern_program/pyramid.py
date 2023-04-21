# # inp=int(input("entet"))
# # for i in range(0, inp):
# #     for j in range(0, inp- 1):
# #         print("")
# #         for k in range(0,j-1):
# #            print("x", end="")
# #     print()  # print("\r")
#
#second method

# def triangle(n):
#     k = n
#     for i in range(0,n):
#         for r in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ",end="")
#         print("\r")
# triangle(6)
#

#third method
inp=int(input("enter the limit level"))
for i in range(1,inp):
    print(" " * (inp-i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

#reverse pyramid
# inp=int(input("enter the reverse limit level"))
# for i in range(inp,0,-1):
#     print(" " * (inp-i) ,end=" ")
#     for j in range(0, i):
#         print("*", end=" ")
#     print()
#
# #second method:
#
# def triangle(n):
#     k = n
#     for i in range(n,0,-1):
#         for r in range(0, k):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, i ):
#             print("* ",end="")
#         print("\r")
# triangle(6)
#
inp=int(input("enter the reverse limit level"))
for i in range(0,inp):
    print(" " * i ,end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()
#

inp=5
for i in range(inp,0,-1):
    print(" "*(inp-i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()


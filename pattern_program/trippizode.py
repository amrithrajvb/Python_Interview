# inp=int(input("enter the reverse limit level"))
# for i in range(inp,0,-1):
#     print(" " * (inp-i) ,end=" ")
#     for j in range(0, i+inp):
#         print("*", end=" ")
#
#     print()
#
# #correct method:
def trapizoid(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k - 1
        for j in range(0, i+5):
            print("* ", end="")
        print("\r")
trapizoid(5)
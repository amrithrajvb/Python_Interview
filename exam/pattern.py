# a=int(input("enter the initial range"))
# # b=int(input("enter the final range"))
# r=5
# for i in range(a,r):
#     if(i%2==0):
#
#         for k in range(r, 0, -1):
#             for j in range(0, k):
#                 print(i,end=" ")
#
#             print("\r")
#     else:
#         for l in range(r):
#             for m in range(0,l+1):
#                 print(i,end=" ")
#             print("\r")





# a=int(input("enter the initial range"))
# # b=int(input("enter the final range"))
# r=5
for i in range(1,5):
    if (i%2==0):

        for k in range(5,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print()
    else:
        for l in range(5):
            for m in range(0,l+1):
                print(i,end=" ")
            print()

# def pattern(n):
#     for i in range(0,n):
#         for j in range(0, i+1):
#             print("*", end="")
#         print()#print("\r")
# pattern(5)

inp=int(input("entet"))
for i in range(0, inp):
    for j in range(0, i + 1):
        print("*", end=" ")
    print()  # print("\r")
 
#pattern(5)
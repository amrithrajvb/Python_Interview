
#while loop

# nterm=10
#
# no1=0
# no2=1
# count=0
# print("finanacci series")
# while count < nterm:
#     print(no1)
#     nth=no1+no2
#     no1=no2
#     no2=nth
#     count +=1

    #for loop
inp= int(input("enter the number"))
no1=0
no2=1
if inp > 0:
    for i in range(inp):
        print(no1)
        add = no1 + no2
        no1 = no2
        no2 = add

else:
    print("please enter postive number")

#         print(no1)
# else:
#     print("")
#     # if sum < add:
#     #     no2= add
#     #     no2=no1
#     #
#     #     sum +=1
#     #     print(add)

# def pattern(row):
#
#     for i in range(0, row):
#         num = 1
#         for j in range(0, i + 1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")
# pattern(5)
#
#
# def pattern(row):
#
#     for i in range(row,0,-1):
#         num = 1
#         for j in range(0, i ):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")
# pattern(5)
#
#
#
#
#
#
#
#
#
#
#


def patterns(b):

    for i in range(0,b):
        num = 1
        for j in range(0,i+1):
            print(num,end=" ")
            num = num+ 1
        print("\r")


patterns(4)
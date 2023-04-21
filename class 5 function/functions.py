# # set of code of execution for reusability
# #definition def
# def add():
#     num1=int(input("enter the number1"))
#     num2=int(input("enter the number2"))
#     print(num1+num2)
#
# add()
#
# #we can use the function multiple time-reusable


def removeBrakets(str):
    n = len(str)
    k=[]
    c=""
    for j in str:
        k.append(j)
    cnt = 0
    if (str[cnt] == '(' ):
        k.pop(cnt)
        for m in k:
          c=c+m

    print(k)
    # print(k)



if __name__=='__main__':
    str="a)b(c)d)"

    removeBrakets(str)

#data structure......store data
#stack
#stackopertions
#1.push....add data
#2.pop....removedata
#last in first out...LIFO
# lis=[]
# inp=int(input("enter the size"))
count=0
# for i in range(inp):
#     c=int(input("eneter the operation want to perform"
#             "press 1)push 2)pop 3)display"))
#     if c in (1,2,3):


#         if c==1:
#             e = int(input("enter the element to be insert"))
#             lis.append(e)
#             count+=1
#
#
#
#         elif c==2:
#             lis.pop()
#             if len(lis)==0:
#                 print("no elements to be delete")
#
#
#
#         elif c==3:
#             print(lis)
#     else:
#         print("enter the correct option")


#Luminar

stk=[]
size=int(input("enter the size"))
top=0
n=0
def push():
    global top,size
    if (top>size):
        print("stack is full")
    else:
        x=int(input("enter the element want to push"))
        stk.append(x)
        top+=1
def pop():
    global top,size
    if (top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
def disply():
    print(stk)

while(n!=1):
    c = int(input("eneter the operation want to perform"
                  "press 1)push 2)pop 3)display"))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        disply()
    n=int(input("do you want to continue press 1 for exit"))






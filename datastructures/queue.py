#insertion....enqueue
#deletion...dequeue
#first in first out...FIFO
# stk=[]
# size=int(input("enter the size"))
# first=0
# n=0
# def Enqueue():
#     global first,size
#     if (first>size):
#         print("queue completed")
#     else:
#         c=int(input("enter the element want to push"))
#         stk.append(c)
#         #
#         first+=1
# def Deque():
#     global first,size
#     if (first<=0):
#         print("queue is empty")
#     else:
#         stk.pop(0)
#         first-=1
# def Disply():
#     print(stk)
#
#
# while(n!=1):
#     c = int(input("enter the operation want to perform"
#                   "press 1)Enqueue 2)Dequeue 3)display"))
#     if c == 1:
#         Enqueue()
#     elif c == 2:
#         Deque()
#     elif c == 3:
#         Disply()
#     n = int(input("do you want to continue press 1 for exit"))



#lUMINAR

# que=[]
# size=int(input("enter the size"))
# rear=0
# front=0
# n=0
# def insert():
#     global front,rear,size,que
#     if rear >=size:
#         print("queue is full")
#     else:
#         p=int(input("enter thge element to be insert"))
#         que.insert(rear,p)
#         rear+=1
#         for i in range(front,rear):
#             print(que[i])
# def delete():
#     global front, rear, size, que
#     if rear==front:
#         print("queue is empty")
#     else:
#         front +=1
#         for i in range(front,rear):
#             print(que[i])
# while(n!=1):
#     c = int(input("enter the operation want to perform"
#                   "press 1)Enqueue 2)Dequeue 3)display"))
#     if c==1:
#         insert()
#     if c==2:
#         delete()


stk=[]
first=0
n=0
size=int(input("enter the size"))
def enqueue():
    global first,size
    if(first>size):
        print("q is completed")
    else:
        inp=int(input("enter the number"))
        stk.append(inp)
        first+=1

def dequeue():
    global first,size
    if(first<=0):
        print("q is empty:")
    else:
        stk.pop(0)
        first-=1

def Disply():
    print(stk)

while(n!=1):
    c = int(input("enter the operation want to perform"
                  "press 1)Enqueue 2)Dequeue 3)display"))
    if c ==1:
        enqueue()
    elif c==2:
        dequeue()
    elif c==3:
        Disply()
    n=int(input("enter the 1 for exit"))
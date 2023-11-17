def ac(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")"
                    for x in word.lower()])
print(ac("abA"))





def carpet(words):
    return "".join([" " if x in "aeiou" else x
                    for x in words])

print(carpet("pycharm"))


str = "abcbababc"
test = "abc"
count = 0
for i in range(len(str)-1):
   if str[i] == test[0]:
      if str[i + 1] == test[1]:
         if str[i + 2] == test[2]:
            count = count + 1
            # i = i + 3

print(count)


str1 = "isincisinefsdfsdinedfsdagdhrtsyrine"
str2 = "ine"
len1 =len(str1)
len2 = len(str2)
Count = 0

for i in range(len1 - len2 + 1):
    j = 0
    for k in range(i, i + len2):
        if str1[k] != str2[j]:
            break
        j += 1
    if j == len2:
        Count += 1

print(Count)


a=[i for i in range(101) if i > 1 if all((i%j!=0)for j in range(2,i))]
print(a)


print("-----------------")
data = [1,2,3,[4,[5,6,7,[8,9]]]]

def print_list(the_list):

    for each_item in the_list:
        if isinstance(each_item, list):
            print_list(each_item)
        else:
            print(each_item)

print_list(data)


print("---------------------")






# cLASS METHOD

from datetime import date


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromyearofbirth(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def IsAudult(age):
        return age > 18


# The difference between the Class method and the static method is:
#
# A class method takes cls as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
#

person = Person("arun", 21)
person2 = Person.fromyearofbirth("arun", 1996)

print(person2.name)
print(person.IsAudult(10))

#amstrong
n = 153
temp = n
sum = 0

while temp > 0:
    d = temp % 10
    sum += d ** 3
    temp //= 10

if n == sum:
    print(n, "is amstrong")
else:
    print(n, "is not amstrong ")





#palidrome
n = 354
temp = n
sum = 0

while temp > 0:
    d = temp % 10
    sum = sum * 10 + d
    print(sum)
    temp //= 10
print("sums",sum)

if n == sum:
    print(n, "is palindrome")
else:
    print(n, "is not palindrome")





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

lis = [1, 0, 5, 2, 6, 0, 6, 8]
c = []
# length = len(lis)
# [1,5,2,6,6,8,0,0]
for i in range(len(lis)):
    if lis[i] == 0:
        # c.append(lis[i])
        lis.append(lis[i])

        lis.remove(lis[i])
        # lis[-2]=lis[-1]
        # lis[-1]=lis[i]

print(lis)

str1 = "I am akshay"
output = "akshay am i"
c = ""
# str1 = "I am akshay"[::-1]
# print(str1)
# for i in str1:
#     for j in i:

words = str1.split(" ")
c=words[::-1]
print("rev",c)
print(words[::-1])




c=3
w=12

if(w <=2 or w%2!=0 or c>w) :
    print("invalid output")
else:
    x=(4*c -w)//2
print("tw",x,"fw",c-x,)




def longestPalindrome(s):
    if (s == s[::-1]):
        return s

    else:
        return max([longestPalindrome(s[1:]), longestPalindrome(s[:-1])], key=len)


print(longestPalindrome("babad"))




# import threading

from threading import *

from time import sleep


def print_cube(num):
    # function to print cube of given num
    print("Cube: {}".format(num * num * num))


def print_square(num):
    # function to print square of given num
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(20,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")


# class cases

class A(Thread):
    def run(self):
        for i in range(5):
            print("hai")
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(5):
            print("halo")
            sleep(1)

t1=A()
t2=B()
t1.start()
t2.start()



# import threading
import time

def print_numbers():
    for i in range(1,6):
        print("Printing number {}".format(i))
        time.sleep(1)

def print_letters():
    for i in "covid":
        print("print letters {}".format(i))
        time.sleep(1)

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t1.start()
t2.start()
t1.join()
t2.join()


#unittesting
import unittest

class Test_new(unittest.TestCase):

    def sums(self,num1,num2):
        return num1+num2

    def setUp(self):
        print("start")
        self.a=20
        self.b=30

    def test_case1(self):
        print("hai")
        result=self.sums(self.a,self.b)
        self.assertEqual(result,self.a+self.b)

    def test_case2(self):
        print("hai")


if __name__=="__main__":
    unittest.main()


#multithreading


import threading
import time

def print_numbers():
    for i in range(1,6):
        print("Printing number {}".format(i))
        time.sleep(1)

def print_letters():
    for i in "covid":
        print("print letters {}".format(i))
        time.sleep(1)

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t1.start()
t2.start()
t1.join()
t2.join()



#multiprocessing
import multiprocessing


def squre(x):
    return x * x


if __name__ == "__main__":
    numbers = [2, 4, 5, 6, 8]

    with multiprocessing.Pool() as pool:
        result = pool.map(squre, numbers)
    print(result)
#
#async
import asyncio
import nest_asyncio
async def greet(name):
	await asyncio.sleep(1)
	print(name)
async def main():
	await asyncio.gather(greet("Geeks"), greet("For"), greet("Geeks"))
# If in a Jupyter notebook or IPython environment:

nest_asyncio.apply()
if __name__ == "__main__":
	asyncio.create_task(main())
#
#Generator
def tasks(n):
    value = 0

    while value < n:
        yield value
        value += 1


for i in tasks(4):
    print(i)
#

# dict={'name':'amrith','age':12,'class':8}
# #dont repeat key's values but repeat values.and not case sensitive.
# #keep the same type
# #mutable
# #all key are consider as string but is not applicatble for values
# print(dict)
# print(type(dict))
# print("Dict[name]",dict['name'])
# print(dict['age'])
#
# #empty dictionary
#
# dic={}
# print(dic)
#
# #updating values
#
# dict1={'name':'amrith','age':12,'class':8}
# dict1['name']='arun'
# print(dict1)

# dict1={"name":"arjun","age":12}
# dict1.update({"loc":"palakkad","company":"ust"})
# print(dict1)
# del dict1["loc"]
# print(dict1)



# # #add keyvalue
# dict1['number']=558555555
# # dict1['mom']="sara"
# print(dict1)
#
#
#
#
#
#
#
#
#
# #
# # #update
# #
# dict1.update({'location':'kochi'})
# print(dict1)
# #
# #
# # #key remove
# # del dict1['location'] #remove element with key value
# # dict1.clear()  #to clear all elements
# # del dict1    #delete entire dictionary
# # print(dict1)
#
# #integer value
# dicc={0:10,2:30}
# print(dicc)
# dicc.update({4:200})
# print(dicc)


#nesting

# a={1:2,{6:7}} #not possiblea={1:2,6:{7,6}}
# print(a)
import calendar
#
#
# def dicts(z):
#     d={}
#     for i in range(z):
#         a = input("sdasf")
#         b = input("adfdf")
#         d[a] = b
#     print(d)
# c=int(input("enter the limit"))
# dicts(c)
#
str = 'coldd'
# dic={}
# i=0
# # enumerate()
# list_enumerate = dict(list(enumerate(str)))
# print(list_enumerate)
#
# i+=1

m={}.fromkeys(["maths","eng","sc"],0)
print(m)

d={ x:x**2 for x in range(6) if x%2==0}
print(d)
# c={x:x*x for x in range(6)}
# print(c)
#
#
# d={x:x*x for x in range(5)}
# print(d)


# Demonstration of list insert() method

a=[]
a.append(str)
print(list(set(a)))
odd = [1, 9,8,7]
c=[10,44,9]
print(list(set(odd + c)))
# a=list(filter(lambda x:x%2==0,odd))
# print(a)
#
# print(odd)

my_dict = {"java": 100, "python": 112, "c": 11}
def searchs(a):
    for key,values in my_dict.items():
        if a==key:
            return values
    return "doesn't exist"


inp=input("enter the key")
print(searchs(inp))

#
# def sample(val):
#     for key, value in my_dict.items():
#         if val == value:
#             return key
#     return "not exist"
#
#
# inp = int(input("enter the key"))
# print(sample(inp))
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
# #add keyvalue
# dict1['number']=558555555
# dict1['mom']="sara"
# print(dict1)
#
# #update
#
# dict1.update({'location':'kochi'})
# print(dict1)
#
#
# #key remove
# del dict1['location'] #remove element with key value
# dict1.clear()  #to clear all elements
# del dict1    #delete entire dictionary
# print(dict1)

#integer value
dicc={0:10,2:30}
print(dicc)
dicc.update({4:200})
print(dicc)


#nesting

#a={1:2,{6:7}}#not possiblea={1:2,6:{7,6}}
#print(a)
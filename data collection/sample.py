import pandas as pd

import xml.etree.cElementTree as ET

# root = ET.Element("root")
# doc = ET.SubElement(root, "doc")
#
# ET.SubElement(doc, "field1", name="blah").text = "some value1"
# ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
#
# tree = ET.ElementTree(root)
# tree.write("filename.xml")
#
# # to read csv file named "samplee"
a = pd.read_csv("input.txt", sep="|")
# a = pd.read_xml("Table.xml")
print(type(a))
# # to save as html file
# # named as "Table"
a.style.format({"dob": lambda t: t.strftime("%m/%d/%Y")})
a.to_xml("Table.xml")
#
# # assign it to a
# # variable (string)
html_file = a.to_xml()




a = pd.read_xml("Table.xml")
# a = pd.read_xml("Table.xml")
#
# # to save as html file
# # named as "Table"
# a['DOB'] = pd.to_datetime(a.dob)
a.style.format({"dob": lambda t: t.strftime("%m/%d/%Y")})
print(a)
a.to_csv("data.csv",index=False)



a = pd.read_csv("data.csv")
# a = pd.read_xml("Table.xml")
#
# # to save as html file
# # named as "Table"
# a['DOB'] = pd.to_datetime(a.dob)
a.style.format({"dob": lambda t: t.strftime("%d/%m/%Y")})
print(a)
a.to_xml("new_data.xml",index=False)
# #
# # # assign it to a
# # # variable (string)
# html_file = a.to_csv()

# #
# from bs4 import BeautifulSoup
#
# # Reading the data inside the xml
# # file to a variable under the name
# # data
# with open('Table.xml', 'r') as f:
#     data = f.read()
#
# csv=open('data.csv','w')
#
# # Passing the stored data inside
# # the beautifulsoup parser, storing
# # the returned object
# Bs_data = BeautifulSoup(data, "xml")
#
# # Finding all instances of tag
# # `unique`
# b_unique = Bs_data.find_all()
# # Bs_d.to_csv ("Test.csv",
# #                   index = None,
# #                   header=True)
# # csv_file=data.to_csv()
# print(b_unique)
# # csv.write()
# #
# # with open("Table.xml","wb") as f:
# #     f.write()
#
#
# from xml.etree import ElementTree
# import csv
#
# # PARSE XML
# xml = ElementTree.parse("Table.xml")
#
# # CREATE CSV FILE
# csvfile = open("data.csv", 'w', encoding='utf-8')
# csvfile_writer = csv.writer(csvfile)
#
# # ADD THE HEADER TO CSV FILE
# csvfile_writer.writerow(["name","age","dob","no"])
#
# # FOR EACH EMPLOYEE
# for employee in xml.findall():
#
#     if (employee):
#         # EXTRACT EMPLOYEE DETAILS
#         name = employee.find("name")
#         age = employee.find("age")
#         dob = employee.find("dob")
#         no = employee.find("no")
#         csv_line = [name.text, age.text, age.text,no.text]
#
#         # ADD A NEW ROW TO CSV FILE
#         csvfile_writer.writerow(csv_line)
# csvfile.close()
import pytesseract


import cv2

img=cv2.imread(r'text.jpg')
# Get text in the image
text=pytesseract.image_to_string(img)

if (2>3) or (2>1):
    print(text)
print(text)
# Convert string into hexadecimal
# hex_text = text.encode("hex")

# print(hex_text)

# import PyPDF2
# import csv
# import sys
# import glob
# import errno
# import json
#
#
# def isnumeric(s):
#     return all(c in "0123456789." for c in s) and any(c in "0123456789" for c in s)
#
# path = '*.pdf'
# files = glob.glob(path)
#
#
# for name in files:
#     read_pdf = PyPDF2.PdfFileReader(name)
#     number_of_pages = read_pdf.getNumPages()
#     page = read_pdf.getPage(3)
#     page_content = page.extractText()
#
#     aa=page_content.split('\n')
#
#     data=[]
#
#     dic={
#         "Title": "PITCH PERPECT",
#         "Title_id": "FM33106746",
#         "Genre": "Film",
#         "Actor": "ANNA KENDRICK/SKYLAR ASTIN",
#         "Production Co": "BROWNSTONE PRODUCTIONS (III)",
#         "Director": "JASON MOORE",
#         "Screenwriter":"",
#         "Country of Origin": "UNITED STATES OF AMERICA",
#         "Production year": "2012",
#         "Production Duration": "112 00",
#         "Music Duration": "87.21"
#     }
#
#     st_point=-1
#     j = 0
#
#     for cur in aa:
#         data.append(cur)
#         j=j+1
#
#         if cur=="Owner(s) of Copyright ":
#             st_point=j
#
#     flag=0
#     read_num=0
#     num=0
#     tot=0
#     ins=[]
#     ins.append([])
#     trac=[]
#
#     for k in range(st_point, j):
#         if flag==1:
#             flag=0
#             if len(data[k])>1 and data[k]!="CA":
#                 str=data[k]
#                 str1=str[0:1]
#                 ins[tot].append(str1)
#                 str1=str[1:len(str)]
#                 ins.append([])
#                 if read_num==1:
#                     read_num=0
#                     trac.append(tot)
#                     ins[tot].append(str1)
#                 else:
#                     ins[tot+1].append(str1)
#                     print(str1)
#                 tot=tot+1
#
#                 if isnumeric(str1):
#                     read_num=1
#
#         else:
#
#             if data[k].isdigit() and len(data)>4:
#                 flag=1
#                 ins[tot].append(data[k])
#             if isnumeric(data[k]) and flag!=1 and read_num==0:
#                 read_num=1
#                 if len(data[k])>6:
#                     str=data[k]
#                     ll = str.find(".")
#                     str1=str[0:ll+3]
#
#                     ins[tot].append(str1)
#                     str1=str[ll+3:len(str)]
#                     ins[tot].append(str1)
#
#
#
#
#     print(len(trac))
#     for ll in trac:
#         print(ll)
#
#
#
# #
# # d = {}
# # aa="Namdfse"
# # d[aa] = "Luke"
# # d["Country"] = "Canada"
# # d["city"]=["asdf","afd"]
# # tt={"ti":"fad", "duf":"dsf"}
# # d["trac"]=tt
# #
# # res=json.dumps(d, indent=4)
# #
# # print(res)
# # f= open("guru99.txt","w+")
# # f.write(res)

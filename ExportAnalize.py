# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:43:20 2021

@author: Alle
"""

# import pandas as pd
# import firebase_admin
# from firebase_admin import credentials, firestore

# cred = credentials.Certificate("D:/Facultate/analize.json")

# firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc_ref = db.collection(u"analize")# Import data
# df = pd.read_csv("D:/Facultate/AnalizeExc.csv")
# tmp = df.to_dict(orient="records")


# list(map(lambda x: doc_ref.add(x), tmp))

# # Export Data
# docs = doc_ref.stream()
# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")

##analize
# import pandas as pd
# import firebase_admin
# from firebase_admin import credentials, firestore

# def mapStringToList(string):
#     if type(string) is float:
#         print(string)
#     lst = string.split(";")
#     newLst = []
#     for elem in lst:
#         parsedElem = elem.strip()
#         newLst.append(parsedElem)
#     return newLst

# def mapNumberToBoolean(number):
#     return True if number == 1 else False

# cred = credentials.Certificate("D:/Facultate/analize.json")

# firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc_ref = db.collection(u"analize")# Import data

# df = pd.read_csv("D:/Facultate/AE.csv")
# tmp = df.to_dict(orient="records")


# for row in tmp:
    
#     for key, value in row.items():
#         if key == "ValScazPosBoli" or key == "ValCrescPosBoli" or key == "Tipul testului" or key == "Valoare Normala(F)" or key =="Valoare Normala(M)":
#             if value != 0:
#                 row[key] = mapStringToList(value)
#         if key == "Exceptie":
#             row[key] = mapNumberToBoolean(value)

# print(tmp)

# list(map(lambda x: doc_ref.add(x), tmp))

#Export Data
# docs = doc_ref.stream()
# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")

##Boli
# import pandas as pd
# import firebase_admin
# from firebase_admin import credentials, firestore

# cred = credentials.Certificate("D:/Facultate/analize.json")

# firebase_admin.initialize_app(cred)

# db = firestore.client()

# df = pd.read_csv("D:/Facultate/BoliOk.csv")
# ids = df['ID'].tolist()
# nb = df['NumeBoala'].tolist()

# res={}
# for key in ids:
#     for value in nb:
#         res[key] = value
#         nb.remove(value)
#         break  
    
# db = firestore.client()
# for i in res:
#     print("I:", i)
#     print("res[]", res[i])
#     a=str(i)
#     # print(a,b)
#     doc_ref = db.collection(u"boli").document(a).set({"ID" : i , "NumeBoala" : res[i]})# Import data

#boli
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

def mapStringToList(string):
    if type(string) is float:
        string="0"
    
    lst = string.split(";")
    newLst = []
    for elem in lst:
        parsedElem = elem.strip()
        newLst.append(parsedElem)
    return newLst

def mapNumberToBoolean(number):
    return True if number == 1 else False

cred = credentials.Certificate("D:/Facultat/boli.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u"boli")# Import data

df = pd.read_csv("D:/Facultate/BoliFinal.csv")
tmp = df.to_dict(orient="records")


for row in tmp:
    
    for key, value in row.items():
        if key == "AnalizeNecesare":
            if value != 0:
                row[key] = mapStringToList(value)


print(tmp)

list(map(lambda x: doc_ref.add(x), tmp))

docs = doc_ref.stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

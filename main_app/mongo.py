from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')
# db = client['Scoredata']
# collec=db['testhistory']
# userid="yogi@mail.com"
# history = { 
#    "user_id":"sample@mail.com",
#    "scores":{ "m1" : {
#         "c/c++" : {
#             "subjectName" : "C/C++",
#             "entryTest" : False,
#             "exitTest" : False
#         },
#         "java" : {
#             "subjectName" : "JAVA",
#             "entryTest" : False,
#             "exitTest" : False
#         },
#         "oops": {
#             "subjectName" : "OOPS",
#             "entryTest" : False,
#             "exitTest" : False
#         },
#         "dsa" : {
#             "subjectName" : "DSA",
#             "entryTest" : False,
#             "exitTest" : False
#         }
#   },
#   "m2" : {
#         "dbms" : {
#             "subjectName" : "DBMS",
#             "entryTest" : False,
#             "exitTest" : False
#         },
#         "cn" : {
#             "subjectName" : "CN",
#             "entryTest" : False,
#             "exitTest" :False
#         },
#         "os" : {
#             "subjectName" : "OS",
#             "entryTest" : False,
#             "exitTest" : False
#         }}
#   }}



def MongoInsertTest(history):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Scoredata']
    collec=db['testhistory']
    id = collec.insert_one(history)
    print(id.inserted_id)


def MongoInsertTotalMark(totmark):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Scoredata']
    collection = db['totalmark']
    id=collection.insert_one(totmark)
    print(id.inserted_id)
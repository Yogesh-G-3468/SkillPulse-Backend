from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['bookstore']
collec=db['books']

history = {
    "m1" : {
        "c/c++" : {
            "subjectName" : "C/C++",
            "entryTest" : False,
            "exitTest" : False,
        },
        "java" : {
            "subjectName" : "JAVA",
            "entryTest" : False,
            "exitTest" : False,
        },
        "oops": {
            "subjectName" : "OOPS",
            "entryTest" : False,
            "exitTest" : False,
        },
        "dsa" : {
            "subjectName" : "DSA",
            "entryTest" : False,
            "exitTest" : False,
        }
    },
    "m2" : {
        "dbms" : {
            "subjectName" : "DBMS",
            "entryTest" : False,
            "exitTest" : False,
        },
        "cn" : {
            "subjectName" : "CN",
            "entryTest" : False,
            "exitTest" :False,
        },
        "os" : {
            "subjectName" : "OS",
            "entryTest" : False,
            "exitTest" : False,
        },
    }
}

for x in collec.find():
    if x['author']== 'JK ROWLING':
        print(x)
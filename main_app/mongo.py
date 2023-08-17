from pymongo import MongoClient
from pymongo.server_api import ServerApi


jumbla = "enter paswrod"


def MongoInsertTest(history):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collec=db['testhistory']
    id = collec.insert_one(history)
    print(id.inserted_id)


def MongoInsertTotalMark(totmark):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    id=collection.insert_one(totmark)
    print(id.inserted_id)




def MongoRetirveTest(userid):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['testhistory']
    for x in collection.find({'user_id':userid}):
        return(x)

def MongoRetirveTotalMarks(userid):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    for x in collection.find({'user_id':userid}):
        return(x)





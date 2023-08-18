from pymongo import MongoClient
from pymongo.server_api import ServerApi


jumbla = "test123"


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


def InsertRating(Indirating):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    if collection.find_one({"user_id":Indirating["user_id"],"subject":Indirating["subject"]})=='None':
        id = collection.insert_one(Indirating)
        print(id.inserted_id)
    else:
        myquery = {"user_id":Indirating["user_id"],"subject":Indirating["subject"]}
        newvalues = { "$set": { "ratings":Indirating['ratings'] } }
        collection.update_one(myquery, newvalues)
        
    
def RetriveRating(userid,subject):
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    x = collection.find_one({"user_id":userid,"subject":subject})
    return x






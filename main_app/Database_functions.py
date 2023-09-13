from pymongo import MongoClient
from pymongo.server_api import ServerApi
import logging
from googlesearch import search
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs.log"),
    ],)
jumbla = "test123"


def MongoInsertTest(history):
    logger = logging.getLogger("MongoInsertTest")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collec=db['testhistory']
    id = collec.insert_one(history)
    logger.info("Inserted id: {}".format(id.inserted_id))

def MongoInsertTotalMark(totmark):
    logger = logging.getLogger("MongoInsertTotalMark")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    id=collection.insert_one(totmark)
    logger.info("Inserted id: {}".format(id.inserted_id))

def MongoUpdateTotalMark(final_mark,userid,testStatus,subject):
    logger = logging.getLogger("MongoUpdateTotalMark")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    myquery = {"user_id":userid}
    path = f"scores.{testStatus}.m2.{subject}"
    newvalues = { "$set": { path:final_mark } }
    collection.update_one(myquery, newvalues)

    
    collection_test_hist = db['testhistory']
    path_status = f"scores.m2.{subject}.{testStatus}"
    path_date = f"scores.m2.{subject}.{testStatus}Completion"
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    new_val_status = { "$set": { path_status:True } }
    new_val_date = { "$set": { path_date:dt_string } }
    collection_test_hist.update_one(myquery, new_val_status)
    collection_test_hist.update_one(myquery, new_val_date)

    
    logger.info("Updated data")



def MongoRetirveTest(userid):
    logger = logging.getLogger("MongoRetirveTest")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['testhistory']
    for x in collection.find({'user_id':userid}):
        logger.info("Retrived data")
        return(x)

def MongoRetirveTotalMarks(userid):
    logger = logging.getLogger("MongoRetirveTotalMarks")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    for x in collection.find({'user_id':userid}):
        logger.info("Retrived data")
        return(x)


def InsertRating(Indirating):
    logger = logging.getLogger("InsertRating")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    if collection.find_one({"user_id":Indirating["user_id"],"subject":Indirating["subject"]})==None:
        id = collection.insert_one(Indirating)
        logger.info("Inserted id: {}".format(id.inserted_id))
    else:
        myquery = {"user_id":Indirating["user_id"],"subject":Indirating["subject"]}
        newvalues = { "$set": { "ratings":Indirating['ratings'] } }
        collection.update_one(myquery, newvalues)
        logger.info("Updated data")
        
    
def RetriveRating(userid,subject):
    logger = logging.getLogger("RetriveRating")
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    x = collection.find_one({"user_id":userid,"subject":subject})
    logger.info("Retrived data")
    return x

def RetriveResources(userid,subject):
    logger = logging.getLogger("RetriveWeakness")
    client =  MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    send=[]
    resources = []
    collection=db['rating']
    x = collection.find_one({"user_id":userid,"subject":subject}) 
    for i in x["ratings"][subject]:
        print("i value:",i)
        send.append(x["ratings"][subject][i]["Weak"])
    print("send:",send)
    for j in send:
        query = subject + " " + j
        print("query:",query)
        for m in  search(query, tld='co.in', lang='en', num=2, start=0, stop=2, pause=2):
            resources.append(m)
    return resources

def SeniorProfiles():
    client =  MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    db= client['seniordata']
    collection=db['profiles']
    x= collection.find("")
    for i in x:
         del i["_id"]
         print(i)
        
print(SeniorProfiles())

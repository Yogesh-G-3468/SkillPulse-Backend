from pymongo import MongoClient
from pymongo.server_api import ServerApi
import logging
import inspect

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs.log"),
    ],)
jumbla = "test123"


def MongoInsertTest(history):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collec=db['testhistory']
    id = collec.insert_one(history)
    logger.info("Inserted id: {}".format(id.inserted_id))

def MongoInsertTotalMark(totmark):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    id=collection.insert_one(totmark)
    logger.info("Inserted id: {}".format(id.inserted_id))

def MongoRetirveTest(userid):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['testhistory']
    for x in collection.find({'user_id':userid}):
        logger.info("Retrived data")
        return(x)

def MongoRetirveTotalMarks(userid):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection = db['totalmark']
    for x in collection.find({'user_id':userid}):
        logger.info("Retrived data")
        return(x)


def InsertRating(Indirating):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    if collection.find_one({"user_id":Indirating["user_id"],"subject":Indirating["subject"]})=='None':
        id = collection.insert_one(Indirating)
        logger.info("Inserted id: {}".format(id.inserted_id))
    else:
        myquery = {"user_id":Indirating["user_id"],"subject":Indirating["subject"]}
        newvalues = { "$set": { "ratings":Indirating['ratings'] } }
        collection.update_one(myquery, newvalues)
        logger.info("Updated data")
        
    
def RetriveRating(userid,subject):
    logger = logging.getLogger(inspect.currentframe().f_code.co_name)
    client = MongoClient('mongodb+srv://test:{}@cluster0.1y89bs5.mongodb.net/?retryWrites=true&w=majority'.format(jumbla),server_api=ServerApi('1'))
    db = client['Scoredata']
    collection=db['rating']
    x = collection.find_one({"user_id":userid,"subject":subject})
    logger.info("Retrived data")
    return x






from pymongo import MongoClient

MONGO_URL = "mongodb+srv://patraavishek900:avishek123@cluster0.exlrw.mongodb.net/resume_analyzer?appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["resume_analyzer"]

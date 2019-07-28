from pymongo import MongoClient
from backend.database.mongo.mongo_codejam_db import MongoCodejamDB
from backend.database.model import *


DB_URL = 'localhost'

raw_client = MongoClient(DB_URL)
client = MongoCodejamDB(DB_URL)

group = InGroup(name="My Group", members=["Yossi", 'Abdul'], password='lol')

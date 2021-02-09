import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.cadastrodb

collection = db.cadastrodb

post1 = {'produto': 'computador', 'marcas':['dell','hp','vaio','lenovo','sony','mac']}

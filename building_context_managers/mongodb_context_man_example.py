"""
    Source from: https://www.geeksforgeeks.org/context-manager-in-python/
"""

# Python program shows the 
# connection management 
# for MongoDB 

from pymongo import MongoClient 

class MongoDBConnectionManager(): 
	def __init__(self, hostname, port): 
		self.hostname = hostname 
		self.port = port 
		self.connection = None

	def __enter__(self): 
		self.connection = MongoClient(self.hostname, self.port) 
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback): 
		self.connection.close() 

# connecting with a localhost 
with MongoDBConnectionManager('localhost', 27017) as mongo: 
	collection = mongo.connection.SampleDb.test
	res = collection.delete_many({'item': "card", 'qty': 15})
	print(f'{res.deleted_count} deleted')
	data = collection.find({'item': "card", 'qty': 15}) 
	collection.insert_one({ 'item': "card", 'qty': 15 })
	for d in data:
		print(d) 

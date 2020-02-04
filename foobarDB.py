import json
import os




class FoobarDB(object):
	def __init__(self, location):
		self.location = os.path.expanduser(location)
		self.load(self.location)


#setting up default location in folder for database
	def load(self, location):
		if os.path.exists(location):
			self._load()
		else:
			self.db = {}
		return True

#load db if found into specific location
	def _load(self):
		self.db = json.load(open(self.location, 'r'))

#function to add values to db
	def dumpdb(self):
		try:
			json.dump(self.db, open(self.location, 'wt'))
			return True
		except:
			return False

# add string value to database
	def set(self, key, value):
		try:
			self.db[str(key)] = value
			self.dumpdb()
			return True
		except Exception as e:
			print("[X] error saving values to database :" + str(e))
			return False

#function to query the database
	def get(self,key):
		try:
			return self.db[key]
		except KeyError:
			print("No value can be found for " + str(key))
			return False


#function to delete specific item in database
	def delete(self, key):
		if not key in self.db:
			return False
		del self.db[key]
		self.dumpdb()
		return True


#function to reset entire database
	def resetdb(self):
		self.db= {}
		self.dumpdb()
		return True

















































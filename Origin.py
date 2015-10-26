from peewee import *
from flask import Flask

class _OriginDBManager:
	def __init__(self, *tables): #table classes
		self.tables = tables
		self._connect_databases(tables)
		self._create_tables(tables)

	def add_tables(self, *tables): #table classes
		self.tables += tables
		self._create_tables(tables)
		self._connect_databases(tables)
		
	def drop_tables(self, *tables):
		for table in tables:
			table.drop_table()
			tables.remove(table)
		
	def _connect_databases(self, tables): 
		self.databases = set([table.Meta.database for table in tables])
		for database in self.databases:
			database.connect()
					
	def _create_tables(self, tables):
		for table in tables:
			try:
				table.create_table()
				print "Table " + table.__name__ + " has been created."
			except OperationalError:
				print "Table " + table.__name__ + " is already in the database. No table was created."
				continue
				
class _OriginAPIManager:
	def __init__(self, name):
		self.app = Flask(name)
		
	def populate(self, *tables):
		pass
		
	def start(self):
		self.app.run()
		
class Origin:
	
	def __init__(self, name, *tables): #table classes
		self.dbManager = _OriginDBManager(*tables)
		self.apiManager = _OriginAPIManager(name)
		
	def add_tables(self, *tables): #table classes. If the table is not in the database, it'll be created first
		self.dbManager.add_tables(*tables)
		
	def drop_tables(self, *tables):
		self.dbManager.drop_tables(*tables)
		
	def start(self):
		self.apiManager.populate(*self.dbManager.tables)
		self.apiManager.start()

from peewee import *
from flask import Flask

class _OriginDBManager:
	def __init__(self, *tables): #table classes
		self.tables = tables
		self._connect_databases(tables) #connects the databases that the tables are affiliated to
		self._create_tables(tables) #if the tables haven't been created before it creates them

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
	
	self.default_methods = ['GET', 'POST', 'PUT', 'DELETE']
	
	def __init__(self, name):
		self.app = Flask(name)
		
	def populate(self, table, methods=default_methods, filter_functions=[(lambda x: x)]):
		
		
		route = '/api/' + table.__name__
		endpoint = route
		self.app.add_url_rule(route, endpoint, function)
		
	def start(self, **options):
		self.app.run(**options)
		
class Origin:
	
	def __init__(self, name, *tables): #table classes
		self.dbManager = _OriginDBManager(*tables)
		self.apiManager = _OriginAPIManager(name)
		
	def add_tables(self, *tables): #table classes. If the table is not in the database, it'll be created first
		self.dbManager.add_tables(*tables)
		
	def drop_tables(self, *tables):
		self.dbManager.drop_tables(*tables)
		
	def _setup_api(self, )
		
	def start(self, **options):
		self.apiManager.populate(*self.dbManager.tables)
		self.apiManager.start(**options)

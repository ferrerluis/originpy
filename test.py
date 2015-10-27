from peewee import Model
from origin import origin

mortalDatabase = SqliteDatabase('mortal.db')
immortalDatabase = SqliteDatabase('immortal.db')

class Mortal(Model):
	class Meta:
		database = mortalDatabase
		
class Immortal(Model):
	class Meta:
		database = immortalDatabase
		
class Human(Mortal):
	birth_date = IntegerField()
	death_date = IntegerField()
	
class God(Immortal):
	awesomeness_rate = IntegerField()
	
def main():
	app = Origin(__name__)
	app.add_tables(Human, God)
	app.start()
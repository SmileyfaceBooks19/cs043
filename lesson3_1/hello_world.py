from lesson2_2.telephone_database import Simpledb

db = Simpledb('recipes.txt')
db.add('relish', 'Pickled cucumber and sugar')
print(db.find('relish'))

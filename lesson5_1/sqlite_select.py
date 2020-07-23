import sqlite3

connection = sqlite3.connect('business.db')

cursor = connection.cursor()

product_cursor = cursor.execute('SELECT * FROM products')
product_list = product_cursor.fetchall()

for product in product_list:
    print(product)

# update
'''connection.execute('UPDATE products SET weight = ?', [9])  # Set all weights to 9
   connection.commit()'''

# delete
'''connection.execute('DELETE FROM products')  # Delete all rows in products
   connection.commit()'''

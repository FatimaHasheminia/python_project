import sqlite3

cnt=sqlite3.connect("shop.db")

#-----------------------------create products table----------------------------

# sql=''' CREATE TABLE products(
#     id INTEGER PRIMARY KEY,
#     pname CHAR(15) NOT NULL,
#     price INTEGER NOT NULL,
#     qnt INTEGER
#     ) '''

# cnt.execute(sql)
# print ("products table has been created")

#------------------------------insert products---------------------------------

# sql=''' INSERT INTO products(pname,price,qnt)
#         VALUES("flower",1200,100) '''
# cnt.execute(sql)
# cnt.commit()
# print ("data inserted!")

#------------------------------create cart table-------------------------------

# sql=''' CREATE TABLE cart(
#     id INTEGER PRIMARY KEY,
#     pid INTEGER NOT NULL,
#     uid INTEGER NOT NULL,
#     qnt INTEGER NOT NULL) '''

# cnt.execute(sql)
# print ("cart table has been created!")


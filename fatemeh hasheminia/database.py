import sqlite3

cnt=sqlite3.connect("shop.db")

#------------------------------create users table------------------------------

# sql=''' CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     user CHAR(15) NOT NULL,
#     pass CHAR(25) NOT NULL,
#     addr CHAR(50),
#     score INTEGER) '''

# cnt.execute(sql)
# print ("table has been created!")

#-----------------------------insert data into table---------------------------

# sql=''' INSERT INTO users(user,pass,addr,score)
#         VALUES("saba","12345678","rasht",80) '''

# cnt.execute(sql)
# cnt.commit()

# user1=input ("username : ")
# pass1=input ("password : ")
# addr1=input ("address : ")
# score1=int (input ("score : "))

# sql=''' INSERT INTO users(user,pass,addr,score)
#         VALUES(?,?,?,?) '''
 
# cnt.execute(sql,(user1,pass1,addr1,score1))
# cnt.commit()

#----------------------------fetch data from table-----------------------------

# sql=''' SELECT user,pass,addr FROM users '''
# sql=''' SELECT * FROM users WHERE (addr="tehran") and (score>10 ) '''

# result=cnt.execute(sql)
# rows=result.fetchall()
# print (rows)
# for item in rows :
#     print (item)

# city=input ("city name : ")
# sql=''' SELECT user,pass FROM users WHERE (addr=?) '''
# result=cnt.execute(sql,(city,))
# rows=result.fetchall()
# print(rows)

# user=input ("please enter a username : ")
# pas=input ("please enter a password : ")
# sql=''' SELECT * FROM users WHERE (user=?) and (pass=?) '''
# result=cnt.execute(sql,(user,pas))
# rows=result.fetchall()
# print(rows)

#------------------------------update table------------------------------------

# sql=''' UPDATE users SET score=10 WHERE user="mandana" '''
# cnt.execute(sql)
# cnt.commit()

#----------------------------delete from table---------------------------------

# sql=''' DELETE FROM users WHERE score=50 '''
# cnt.execute(sql)
# cnt.commit()

#---------------------------receiving information------------------------------

# sql=''' SELECT * FROM users WHERE user like "%ss%" '''
# result=cnt.execute(sql)
# rows=result.fetchall()

# string=input("please enter a username: ")
# string="%"+string+"%"

# sql=''' SELECT * FROM users WHERE user like ? '''
# result=cnt.execute(sql,(string,))
# rows=result.fetchall()
# print(rows)
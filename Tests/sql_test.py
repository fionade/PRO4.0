#!/usr/bin/python
import mysql.connector as mariadb

#Connect, other users are "3d", "laser" and "cnc", all with same password, and full rights to a database with their name.
#Before using, you need to create a table!
# http://192.168.0.10/phpMyAdmin/ "root"  "pro4.0"
# I suggest adding a Primary_Key column with autoincrement so we don't have to worry about that
# + you can specify a column as automatically having the current timestamp as content.
# I did that in one of the existing DBs, check PHP MyAdmin
# followed by just all sensor data


# Connecting
#mariadb_connection = mariadb.connect(user='test', password='test', database='test', host='192.168.0.10')
#mariadb_connection = mariadb.connect(user='root', host='localhost', port = 8889, password='root', database='room')
#mariadb_connection = mariadb.connect(user='printer', password='3d', database='printer', host='192.168.0.10')
mariadb_connection = mariadb.connect(user='laser', password='laser', database='laser', host='192.168.0.10')
cursor = mariadb_connection.cursor()

#Storing information
#Might need to stringify variables beforehand (instead of the dummy numbers I put)

for i in range(0, 5):
    try:
        cursor.execute("INSERT INTO laser_data (sensor,data) VALUES (%s,%s)", ("123",3.14))
    except mariadb.Error as error:
        print("Error: {}".format(error))

#From tutorial, can't replicate its use on MySQL, you need to check on the NAS if it's necessary
mariadb_connection.commit()
print "The last inserted id was: ", cursor.lastrowid

#Finally
mariadb_connection.close()
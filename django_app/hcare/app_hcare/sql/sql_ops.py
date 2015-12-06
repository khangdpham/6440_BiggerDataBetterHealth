import MySQLdb as sqldb
from sql import queries

db = sqldb.connect("localhost","root","","hcare")
cursor = db.cursor()

#create table
my_query = queries["create_table2"]
cursor.execute(my_query)

#select all
#cursor.execute('select * from meds;')
#results = cursor.fetchall()
#print results

#add row
#my_query = queries["add_row2"]
#my_query2 = my_query %(12345678,45,98765,0.85,98764,0.10,98763,0.05)
#cursor.execute(my_query2)
#db.commit()

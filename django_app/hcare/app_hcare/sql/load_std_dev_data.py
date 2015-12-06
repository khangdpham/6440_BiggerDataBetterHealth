import MySQLdb as sqldb
from sql import queries

db_name = "hcare"

db = sqldb.connect("localhost","root","",db_name)
cursor = db.cursor()

with open('../analysis_20151122.csv','r') as f:
    lines = f.readlines()
    lines2 = [x.strip().split(',') for x in lines]
print lines[0]

for record in lines2:
    to_load = queries['add_row'] %(record[0], record[1], record[2], record[3], record[4])  
    #print to_load
    cursor.execute(to_load)

db.commit()
cursor.close()

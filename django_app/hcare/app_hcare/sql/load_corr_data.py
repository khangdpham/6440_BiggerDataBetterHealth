import MySQLdb as sqldb
from sql import queries

db_name = "hcare"

db = sqldb.connect("localhost","root","",db_name)
cursor = db.cursor()

with open('../../../../data_analysis/condition_medication_probs_20151127.csv','r') as f:
    lines = f.readlines()
    lines2 = [x.strip().split(',') for x in lines]


line_len = 8
for record in lines2:
    diff = line_len - len(record)
    if diff:
        record.extend(['NULL' for _ in range(diff)])
    to_load = queries['add_row2'] %tuple([x for x in record])
    cursor.execute(to_load)
db.commit()
cursor.close()

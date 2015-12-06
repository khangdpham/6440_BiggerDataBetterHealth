import MySQLdb as sqldb
db_name='hcare'
db_conn = sqldb.connect("localhost","root","",db_name)
cursor = db_conn.cursor()

#cursor.execute("select * from meds;")
#out = cursor.fetchall()
#cursor.close()

#med_names = [x[-1] for x in out]
#print med_names

#med_ids = [str(x[1]) for x in out]
#print med_ids

cursor.execute("select * from meds_corr;")
out = cursor.fetchall()
cursor.close()


cond_ids = [str(x[1]) for x in out]
print cond_ids

med_ids1 = [x[3] for x in out]
#print med_ids1[:10]

med_ids2 = [x[5] for x in out]
#print med_ids2[:10]

med_ids3 = [x[7] for x in out]
#print med_ids3[:10]

med_ids_all = list(set(med_ids1 + med_ids2 + med_ids3))
med_ids_all.sort()
med_ids_all = [str(x) for x in med_ids_all]
print med_ids_all

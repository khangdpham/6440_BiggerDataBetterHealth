from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect

import MySQLdb as sqldb
import django.db

from sql.sql import queries

from models import Meds, MedsCorr

from re import *

#db_name = "hcare"

#def getsql(sql):
#    db_conn = sqldb.connect("localhost","root","",db_name)
#    cursor = db_conn.cursor()
#    cursor.execute(sql)
#    result = cursor.fetchall()
#    cursor.close()
#    db_conn.close()
#    return result


def main(request):
	return render(request, 'app_hcare/index.html',) 
def about(request):
	return render(request, 'app_hcare/about.html',)

def process_data(request):

	med_id = request.POST['med_id']
	med_name = request.POST['med_name']

	med_id_obj, med_name_obj = False, False
	if med_id:
		try:
			med_id_obj = Meds.objects.get(med_id=med_id)
		except:
			return HttpResponse('Sorry we don\'t have any information for that medication id.')
	if med_name:
		try:
			med_name_obj = Meds.objects.get(name=med_name)
		except:
			return HttpResponse('Sorry we don\'t have any information for that medication name.')
	if not(med_name or med_id):
		return HttpResponse('Please enter a medication or a medication number.')

	if (med_name and med_id) and (med_id_obj.pk !=  med_name_obj.pk):
		return HttpResponse('Sorry, that medication id and medication name don\'t match.')

	med = med_id_obj or med_name_obj
	
	try:
		#dosage = int(request.POST['dosage'])
		raw_dosage = request.POST['dosage']
		raw_dosage = split("\.", raw_dosage)
		dosage = int(sub("\D", "", raw_dosage[0]))
		
	except:
		return HttpResponse('Please enter a dosage.')
	
	std_dev_for_drug = med.std_dev
	mean = med.mean

	if (dosage <= mean + std_dev_for_drug) and (dosage >= mean - std_dev_for_drug):
		return HttpResponse('Good News: Your dosage is within one standard deviation (%s) of the average dosage (%s) prescribed by other doctors.' %(std_dev_for_drug,mean)) 
	else:
		return HttpResponse('Warning: Your dosage is outside of one standard deviation (%s) of the average dosage (%s) prescribed by other doctors.' %(std_dev_for_drug,mean))


def process_data_corr(request):
	cond_id = request.POST['condition_id']
	try:
		med_id = int(request.POST['med_id_for_condition'])
	except:
		return HttpResponse('Please enter a valid numerical medication id.')
	if not(cond_id and med_id):
		return HttpResponse('Please enter both a condition id and medication id.')
	
	try:
		cond_obj = MedsCorr.objects.get(condition_id=cond_id)
	except:
		return HttpResponse('Sorry we don\'t have any information for that condition id.')
	target_meds = [(cond_obj.suggest_med_1,cond_obj.suggest_med_1_prob), (cond_obj.suggest_med_2,cond_obj.suggest_med_2_prob), (cond_obj.suggest_med_3,cond_obj.suggest_med_3_prob)]
	find_med = [(x,y) for x,y in enumerate(target_meds) if y[0] == med_id]
	cond_count = cond_obj.obs_count
	if find_med:
		prob_med = round(find_med[0][1][1],4)*100
		rank_med = find_med[0][0]
		rank_dict = {0:'the most likely to be prescribed medication',1:'the second most likeley to be prescribed medication',2:'the third most likely to be prescribed medication'}
		rank_final = rank_dict[rank_med]
		return HttpResponse('Out of %s medication prescriptions when condition code %s is present, medication %s is %s with a prescription frequency for this condition of %s%%. This is likely a correct prescription!' %(cond_count, cond_id, med_id, rank_final, prob_med))

	recommend_meds =  ",".join([str(x) for x in [cond_obj.suggest_med_1, cond_obj.suggest_med_2, cond_obj.suggest_med_3] if x])
	return HttpResponse('Out of %s medication prescriptions when condition code %s is present, medication %s is not the 1st, 2nd or 3rd most likely medication to be prescribed. This is likely an incorrect prescription!  You might want to consider one of the following meds: %s' %(cond_count, cond_id, med_id, recommend_meds))

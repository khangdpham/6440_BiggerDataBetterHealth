import sys
sys.path.insert(0,'..')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hcare.settings'

from app_hcare.models import Meds
from django.test import TestCase
from app_hcare.views import process_data, process_data_corr
import unittest

class TestProcessData(unittest.TestCase):
	
	def setUp(self):
		
		class request(object):
			def __init__(self, med_id=None, med_name=None, dosage=None):
				self.POST = {'med_id' : med_id, 'med_name': med_name, 'dosage': dosage}
		self.request = request

	def test_process_data(self):
		
		#set up request
		req = self.request(med_id='19019072', dosage='123')
		#test method
		resp = process_data(req)
		#compare
		self.assertEqual(resp.content,'Warning: Your dosage is outside of one standard deviation (0.0) of the average dosage (400.0) prescribed by other doctors.')		

class TestProcessDataCorr(unittest.TestCase):   
	def setUp(self): 
		class request(object): 
		      def __init__(self, med_id=None, cond_id=None): 
			      self.POST = {'med_id_for_condition' : med_id, 'condition_id' : cond_id}
		self.request = request
	
	def test_process_data_corr(self): 
		req = self.request(med_id='955641', cond_id='441456002')
		resp = process_data_corr(req)
		self.assertEqual(resp.content, 'Out of 16 medication prescriptions when condition code 441456002 is present, medication 955641 is the most prescribed medication with a prescription frequency for this condition of 50.0%. This is likely a correct prescription!')

if __name__ == '__main__':
    unittest.main()

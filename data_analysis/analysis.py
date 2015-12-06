# Operates directly on the XML output from http_get_batch. Generates a CSV of the format:
# medication_number,instances_count,mean,std,name
# medication_number = integer id
# instances_count = integer number of times this medication_number appeared in the data set.
# mean = float meat of all medication prescribed dosage values
# std = float std of all medication prescribed dosage values
# name = string descriptive name

import xml.etree.ElementTree as etree
from collections import defaultdict
import numpy as np
import urllib2

tree = etree.parse('MedicationPrescription.xml')
root = tree.getroot()

MedicationPrescription = defaultdict(list)

for child in root:
    if child.tag[-5:] == 'entry':
        for child in child:
            if child.tag[-8:] == 'resource':
                for child in child:
                    if child.tag[-22:] == 'MedicationPrescription':
                        number = []
                        value = []
                        for child in child:

                            if child.tag[-10:] == 'medication':
                                for child in child:
                                    if child.tag[-9:] == 'reference':
                                        number = int(child.attrib['value'][11:])
                            if child.tag[-17:] == 'dosageInstruction':
                                for child in child:
                                    if child.tag[-12:] == 'doseQuantity':
                                        for child in child:
                                            if child.tag[-5:] == 'value':
                                                value = float(child.attrib['value'])
                        if number and value:
                            MedicationPrescription[number].append(value)

file_output = open('medication_stats.csv','w')
for medication in MedicationPrescription:
    file_object = open('Medication.xml','w')
    url = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp-ro/base/Medication?_id=" + str(medication) + "&_format=xml&_pretty=true"
    data = urllib2.urlopen(url).read()
    file_object.write(data)
    file_object.close()

    tree = etree.parse('Medication.xml')
    root = tree.getroot()
    name = root[6][0][0][2].attrib['value'].replace(","," ")
    print "medication:" + str(medication) + " instances:" + str(len(MedicationPrescription[medication])) + " mean:" + str(np.mean(MedicationPrescription[medication])) + " std:" + str(np.std(MedicationPrescription[medication])) + " name:" + name

    file_output.write(str(medication) + "," + str(len(MedicationPrescription[medication])) + "," + str(np.mean(MedicationPrescription[medication])) + "," + str(np.std(MedicationPrescription[medication])) + "," + name + "\n")

file_object.close()

#cond = np.genfromtxt('Condition.csv', delimiter=',')
# rx_all = np.genfromtxt('MedicationPrescription.csv', delimiter=',')
#
# rx_uniq = np.unique(rx_all[:,3])
#
# for rx in rx_uniq:
#     rx_dosages = rx_all[rx_all[:,3] == rx][:,4]
#     print "rx: " + str(rx) + " samples: " + str(len(rx_dosages)) + " dosage mean: " + str(np.mean(rx_dosages)) + " dosage std: " + str(np.std(rx_dosages))

import urllib2

# The FHIR DB RO medication resource returns HTTP errors for entries 350 to 399, so this won't work currently.
# file_object = open('Medication.xml','w')
# offset = 0
# count = 50
# total = 222828
# getpages = "c0552b97-92f2-4a82-8290-dfa9c6aceaf0"
# string1 = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp-ro/base?_getpages=" + getpages
# string2 = "&_getpagesoffset=" + str(offset)
# string3 = "&_count=" + str(count)
# string4 = "&_format=xml&_pretty=true"
# url = string1 + string2 + string3 + string4
# data = urllib2.urlopen(url).read()
# file_object.write(data[0:data.find('<entry>')])
# for offset in range(0,total,count):
#     print "MedicationPrescription offset: " + str(offset)
#     string2 = "&_getpagesoffset=" + str(offset)
#     url = string1 + string2 + string3 + string4
#     data = urllib2.urlopen(url).read()
#     file_object.write(data[data.find('<entry>'):data.find('</Bundle>')])
# file_object.write(data[data.find('</Bundle>'):])
# file_object.close()

# Replace getpages with your session key.
file_object = open('MedicationPrescription.xml','w')
offset = 0
count = 50
total = 1697
getpages = "5d2085c6-5f49-498a-b81e-5abfa092025e"
string1 = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp-ro/base?_getpages=" + getpages
string2 = "&_getpagesoffset=" + str(offset)
string3 = "&_count=" + str(count)
string4 = "&_format=xml&_pretty=true"
url = string1 + string2 + string3 + string4
data = urllib2.urlopen(url).read()
file_object.write(data[0:data.find('<entry>')])
for offset in range(0,total,count):
    print "MedicationPrescription offset: " + str(offset)
    string2 = "&_getpagesoffset=" + str(offset)
    url = string1 + string2 + string3 + string4
    data = urllib2.urlopen(url).read()
    file_object.write(data[data.find('<entry>'):data.find('</Bundle>')])
file_object.write(data[data.find('</Bundle>'):])
file_object.close()

# Replace getpages with your session key.
file_object = open('Condition.xml','w')
offset = 0
count = 50
total = 3178
getpages = "6fdb1bf0-6220-420c-b903-717e7c7ae789"
string1 = "http://polaris.i3l.gatech.edu:8080/gt-fhir-webapp-ro/base?_getpages=" + getpages
string2 = "&_getpagesoffset=" + str(offset)
string3 = "&_count=" + str(count)
string4 = "&_format=xml&_pretty=true"
url = string1 + string2 + string3 + string4
data = urllib2.urlopen(url).read()
file_object.write(data[0:data.find('<entry>')])
for offset in range(0,total,count):
    print "Condition offset: " + str(offset)
    string2 = "&_getpagesoffset=" + str(offset)
    url = string1 + string2 + string3 + string4
    data = urllib2.urlopen(url).read()
    file_object.write(data[data.find('<entry>'):data.find('</Bundle>')])
file_object.write(data[data.find('</Bundle>'):])
file_object.close()


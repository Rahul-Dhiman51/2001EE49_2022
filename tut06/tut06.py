from datetime import datetime
from unicodedata import name
start_time = datetime.now()

def attendance_report():
        ##code starts from here
 import csv
 import os
 import numpy as np
 os.system('cls')
 roll_numbers=[]
 students_name=[]

 with open('input_registered_students.csv', 'r') as f:
  reader = csv.reader(f)
  r=0
  for row in reader:
   if r!=0:
    roll_numbers.append(row[0])
    students_name.append(row[1])
   r=r+1
  r=r-1
 lec_dates =["28/07","01/08","04/08","08/08","11/08","15/08","18/08","22/08","25/08","29/08","01/09","05/09","08/09","12/09","15/09","26/09","29/09"]
 num_of_days=len(lec_dates)

 with open('input_attendance.csv', 'r') as f:
  reader = csv.reader(f) 

  all_data=[] #stores all data of all the students for all dates
  sinle_data=[] #stores all data of particular student of all dates
  part_date_single_data=[]  #stores all data of particular student on particular date
  for x in roll_numbers:
   sinle_data=[]
   for j in lec_dates:
    part_date_single_data=[]
    ct1=0
    ct2=0
    ct3=0
    with open('input_attendance.csv', 'r') as f:
     reader = csv.reader(f)
     for row in reader:
      if j==row[0][0:5] and row[1][0:8]==x and (row[0][11:13]=="14" or row[0][11:16]=="15:00" ) and ct1==0 : 
       ct1=ct1+1
      elif j==row[0][0:5] and row[1][0:8]==x and (row[0][11:13]=="14" or row[0][11:16]=="15:00") and ct1>0 : 
       ct2=ct2+1
      elif j==row[0][0:5] and row[1][0:8]==x :
       ct3=ct3+1

attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

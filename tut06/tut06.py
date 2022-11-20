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



attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

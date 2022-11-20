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
     part_date_single_data.append(ct1+ct2+ct3)  
     part_date_single_data.append(ct1)
     part_date_single_data.append(ct2)
     part_date_single_data.append(ct3)
     if ct1==0:
      part_date_single_data.append(1)
     else:
      part_date_single_data.append(0) 
    sinle_data.append(part_date_single_data)
   all_data.append(sinle_data)
 
 print(all_data[0])

 if os.path.exists("output"):
  for f in os.listdir("output"):
    os.remove(os.path.join("output",f))

 os.chdir("output")
 from openpyxl import Workbook
 for i in range(0,r): 
  book=Workbook()
  spreadsheet= book.active    
  rows=[] 
  rows.append(["Date","Roll No.","Name","Total attendance count","Real","Duplicate","Invalid","absent"])
  rows.append(["",roll_numbers[i],students_name[i],"","","","",""])
  for q in range(0,num_of_days):
   rows.append([lec_dates[q],"","",all_data[i][q][0],all_data[i][q][1],all_data[i][q][2],all_data[i][q][3],all_data[i][q][4]])
  for w in rows:
   spreadsheet.append(w)
  book.save( roll_numbers[i] + ".xlsx")

  dic={0:"A",1:"P"}
  book=Workbook()
  spreadsheet= book.active    
  rows=[]
  l=["Roll No.","Name"]
  for i in lec_dates:
   l.append(i)
  l.append("Total Lecture taken")
  l.append("Total Real")
  l.append("% Attendance")
  rows.append(l) 

  l=["(Sorted by roll no.)","","Atleast one real P"]
  for i in range(0,num_of_days-1):
   l.append("")
  l.append("(=Total Mon+Thur dynamic count")
  l.append("")
  l.append("Real/Actual Lecture taken")
  rows.append(l) 

  for i in range(0,r): 
   l=[roll_numbers[i],students_name[i]]
   sinle_data=0
   for q in range(0,num_of_days):
    l.append(dic[all_data[i][q][1]])
    if dic[all_data[i][q][1]]=="P":
     sinle_data=sinle_data+1
   l.append(num_of_days)
   l.append(sinle_data)
   l=(sinle_data/num_of_days)*100
   l.append("{:.2f}".format(l))
   rows.append(l)

  for w in rows:
   spreadsheet.append(w)
  book.save( "Attendance_report_consolidated" + ".xlsx") 

attendance_report()


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
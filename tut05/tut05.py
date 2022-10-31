from datetime import datetime
start_time = datetime.now()

def octant_range_names(mod=5000):
 from openpyxl import load_workbook
 import os
 import numpy as np
 from operator import itemgetter

 os.system('cls')

 d1 = []    # declaring new list
 b1 = []    # declaring new list
 a1 = []    # declaring new list
 c1 = []    # declaring new list
 b2 = []    # declaring list for difference 
 a2 = []    # declaring list for difference
 c2 = []    # declaring list for difference
 octants = []   # declaring list for octant storing

 work_book=load_workbook("octant_input.xlsx")
 spreadsheet=work_book["Sheet1"] 
 num_1=spreadsheet.max_row
 for i in range(2,num_1+1):
  d1.append(spreadsheet.cell(row=i,column=1).value)
  a1.append(spreadsheet.cell(row=i,column=2).value)
  b1.append(spreadsheet.cell(row=i,column=3).value)
  c1.append(spreadsheet.cell(row=i,column=4).value)

 b_mean_value=np.mean(b1, dtype=np.float64) # for mean of b1
 a_mean_value=np.mean(a1, dtype=np.float64) # for mean of a1
 c_mean_value=np.mean(c1, dtype=np.float64) # for mean of c1
 
 for i in range(2,num_1+1):
  a2.append(float(spreadsheet.cell(row=i,column=2).value)-a_mean_value) # pushing the differences 
  b2.append(float(spreadsheet.cell(row=i,column=3).value)-b_mean_value) # pushing the differences
  c2.append(float(spreadsheet.cell(row=i,column=4).value)-c_mean_value)	# pushing the differences  

  # Finding octant with the help of for loop
 for i in range(0,num_1-1):
  if ((a2[i]>=0) and (b2[i]>=0) and (c2[i]>=0 )):
   octants.append(1)
  elif((a2[i]>=0) and (b2[i]>=0) and (c2[i]<0 )):
   octants.append(-1)
  elif((a2[i]<0) and (b2[i]>=0) and (c2[i]>=0 )):
   octants.append(2)
  elif((a2[i]<0) and (b2[i]>=0) and (c2[i]<0 )):
   octants.append(-2)
  elif((a2[i]>=0) and (b2[i]<0) and (c2[i]>=0 )):
   octants.append(4)
  elif((a2[i]>=0) and (b2[i]<0) and (c2[i]<0 )):
   octants.append(-4)    
  elif((a2[i]<0) and (b2[i]<0) and (c2[i]>=0 )):
   octants.append(3)
  else:
   octants.append(-3) 
     
  ct1=0         # counting of octant 1
  ct2=0         # counting of octant -1
  ct3=0         # counting of octant 2
  ct4=0         # counting of octant -2
  ct5=0         # counting of octant 3
  ct6=0         # counting of octant -3
  ct7=0         # counting of octant 4
  ct8=0         # counting of octant -4

  #finding the octants using loop
 for i in range(0,num_1-1):
  if (octants[i]==1):
   ct1=ct1+1
  elif(octants[i]==-1):
   ct2=ct2+1
  elif(octants[i]==2):
   ct3=ct3+1
  elif(octants[i]==-2):
   ct4=ct4+1
  elif(octants[i]==3):
   ct5=ct5+1
  elif(octants[i]==-3):
   ct6=ct6+1    
  elif(octants[i]==4):
   ct7=ct7+1
  else:
   ct8=ct8+1

    
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}





mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
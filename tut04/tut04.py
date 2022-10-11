def octant_longest_subsequence_count_with_range():
 from openpyxl import load_workbook
 import os
 import numpy as np
 os.system('cls')

 d1 = []    # declaring new list
 b1 = []    # declaring new list
 a1 = []    # declaring new list
 c1 = []    # declaring new list
 b2 = []    # declaring list for difference 
 a2 = []    # declaring list for difference
 c2 = []    # declaring list for difference
 octants = []   # declaring list for octant storing

 work_book=load_workbook("input_octant_longest_subsequence_with_range.xlsx")
 spreadsheet=work_book["Sheet1"] 
 num_1=spreadsheet.max_row
 for i in range(2,num_1+1):
  d1.append(spreadsheet.cell(row=i,column=1).value)
  a1.append(spreadsheet.cell(row=i,column=2).value)
  b1.append(spreadsheet.cell(row=i,column=3).value)
  c1.append(spreadsheet.cell(row=i,column=4).value)

 b_mean_value=np.mean(b1, dtype=np.float64)     # mean of b1
 a_mean_value=np.mean(a1, dtype=np.float64)     # mean of a1
 c_mean_value=np.mean(c1, dtype=np.float64)     # mean of c1

    #appending the differences..............
 for i in range(2,num_1+1):
  a2.append(float(spreadsheet.cell(row=i,column=2).value)-a_mean_value) 
  b2.append(float(spreadsheet.cell(row=i,column=3).value)-b_mean_value)
  c2.append(float(spreadsheet.cell(row=i,column=4).value)-c_mean_value) 

    #Finding the octant with the help of for loop
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

 lss1=0         # storing the longest subsequence value of octant 1
 lss2=0         # storing the longest subsequence value of octant -1
 lss3=0         # storing the longest subsequence value of octant 2
 lss4=0         # storing the longest subsequence value of octant -2
 lss5=0         # storing the longest subsequence value of octant 3
 lss6=0         # storing the longest subsequence value of octant -3
 lss7=0         # storing the longest subsequence value of octant 4
 lss8=0         # storing the longest subsequence value of octant -4

 lssl1=0        # for storing length of the longest subsequence length for octant 1
 lssl2=0        # for storing length of the longest subsequence length for octant -1
 lssl3=0        # for storing length of the longest subsequence length for octant 2
 lssl4=0        # for storing length of the longest subsequence length for octant -2
 lssl5=0        # for storing length of the longest subsequence length for octant 3
 lssl6=0        # for storing length of the longest subsequence length for octant -3
 lssl7=0        # for storing length of the longest subsequence length for octanlss8 4
 lssl8=0        # for storing length of the longest subsequence length for octant -4

 ct1=0          # counting of octant 1
 ct2=0          # counting of octant -1
 ct3=0          # counting of octant 2
 ct4=0          # counting of octant -2
 ct5=0          # counting of octant 3
 ct6=0          # counting of octant -3
 ct7=0          # counting of octant 4
 ct8=0          # counting of octant -4





#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

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
 ranks=[]
 rank1_idname=[]
 reqrd=[]
 reqrd.append([ct1,1])
 reqrd.append([ct2,2])
 reqrd.append([ct3,3])
 reqrd.append([ct4,4])
 reqrd.append([ct5,5])
 reqrd.append([ct6,6])
 reqrd.append([ct7,7])
 reqrd.append([ct8,8]) 

 reqrd.sort()

 reqrd_ranks=[0,0,0,0,0,0,0,0]
 reqrd_ranks[reqrd[0][1]-1]=8
 reqrd_ranks[reqrd[1][1]-1]=7
 reqrd_ranks[reqrd[2][1]-1]=6
 reqrd_ranks[reqrd[3][1]-1]=5
 reqrd_ranks[reqrd[4][1]-1]=4
 reqrd_ranks[reqrd[5][1]-1]=3
 reqrd_ranks[reqrd[6][1]-1]=2
 reqrd_ranks[reqrd[7][1]-1]=1
 ranks.append(reqrd_ranks)

 rank_idname=[]

 if reqrd_ranks[0]==1:
  rank_idname=[1,"Internal outward Interaction"]
  rank1_idname.append(rank_idname)
 elif reqrd_ranks[1]==1:
  rank_idname=[-1,"External outward Interaction"]
  rank1_idname.append(rank_idname)
 elif reqrd_ranks[2]==1:
  rank_idname=[2,"External Ejection"]
  rank1_idname.append(rank_idname) 
 elif reqrd_ranks[3]==1:
  rank_idname=[-2,"Internal Ejection"]
  rank1_idname.append(rank_idname) 
 elif reqrd_ranks[4]==1:
  rank_idname=[3,"External inward Interaction"]
  rank1_idname.append(rank_idname) 
 elif reqrd_ranks[5]==1:
  rank_idname=[-3,"Internal inward Interaction"]
  rank1_idname.append(rank_idname) 
 elif reqrd_ranks[6]==1:
  rank_idname=[4,"Internal Sweep"]
  rank1_idname.append(rank_idname) 
 elif reqrd_ranks[7]==1:
  rank_idname=[-4,"External Sweep"]
  rank1_idname.append(rank_idname) 

 # Making lists of different octants in mod range

 octants_ct1=[]      
 octants_ct2=[] 
 octants_ct3=[]     
 octants_ct4=[]
 octants_ct5=[]
 octants_ct6=[] 
 octants_ct7=[]
 octants_ct8=[]

  #count of octants in mod range...

 oct_1=0 
 oct_2=0
 oct_3=0
 oct_4=0
 oct_5=0
 oct_6=0
 oct_7=0
 oct_8=0

 k= int((num_1-2)/mod) +1     # k gives the value of interval.
 sn_1=0
 sn_2=0
 sn_3=0
 sn_4=0
 sn_5=0
 sn_6=0
 sn_7=0
 sn_8=0
  
 for i in range(k):
  y=mod*i
  for j in range(mod):	
   if(j+y<num_1-1):	                                    
    if (octants[j+y]==1):
     oct_1=oct_1+1 
    elif(octants[j+y]==-1):
     oct_2=oct_2+1
    elif(octants[j+y]==2):
     oct_3=oct_3+1
    elif(octants[j+y]==-2):
     oct_4=oct_4+1
    elif(octants[j+y]==3):
     oct_5=oct_5+1
    elif(octants[j+y]==-3):
     oct_6=oct_6+1    
    elif(octants[j+y]==4):
     oct_7=oct_7+1
    elif(octants[j+y]==-4):
     oct_8=oct_8+1

  octants_ct1.append(oct_1)
  octants_ct2.append(oct_2) 
  octants_ct3.append(oct_3)
  octants_ct4.append(oct_4)
  octants_ct5.append(oct_5)
  octants_ct6.append(oct_6)
  octants_ct7.append(oct_7)
  octants_ct8.append(oct_8)




mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
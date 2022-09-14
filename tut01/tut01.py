def octact_identification(mod=5000):
 import csv
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
 with open('octant_input.csv', 'r') as file:    #opening input file.
  reader = csv.reader(file)
  t = 0
  for row in reader:
   if (t == 0):
    t = t+1 # continue only for t==0
   else:
    d1.append(row[0])
    a1.append(row[1])
    b1.append(row[2])
    c1.append(row[3])
  b_mean_value=np.mean(b1, dtype=np.float64) # for mean of b1
  a_mean_value=np.mean(a1, dtype=np.float64) # for mean of a1
  c_mean_value=np.mean(c1, dtype=np.float64) # for mean of c1

 with open('octant_input.csv', 'r') as file: # reopening input file
  reader = csv.reader(file)
  k=0
  for row in reader:
   if (k==0):
    k=k+1
   else:
    a2.append(float(row[1])-a_mean_value)
    b2.append(float(row[2])-b_mean_value)
    c2.append(float(row[3])-c_mean_value)	

 with open('octant_input.csv', 'r') as file:
  reader = csv.reader(file)
  l=0           # counting the number of rows.
  for row in reader:
   l=l+1
  rows=l        # rows are number of rows
  rows=rows-1
  print(rows)
 with open('octant_input.csv', 'r') as file:    #opening file for octants..
  reader = csv.reader(file)  
 	
  for l in range(rows):     #finding the octants using loop
   if (l<rows-1):
    if ((a2[l]>=0) and (b2[l]>=0) and (c2[l]>=0 )):
     octants.append(1)
    elif((a2[l]>=0) and (b2[l]>=0) and (c2[l]<0 )):
     octants.append(-1)
    elif((a2[l]<0) and (b2[l]>=0) and (c2[l]>=0 )):
     octants.append(2)
    elif((a2[l]<0) and (b2[l]>=0) and (c2[l]<0 )):
     octants.append(-2)
    elif((a2[l]>=0) and (b2[l]<0) and (c2[l]>=0 )):
     octants.append(4)
    elif((a2[l]>=0) and (b2[l]<0) and (c2[l]<0 )):
     octants.append(-4)    
    elif((a2[l]<0) and (b2[l]<0) and (c2[l]>=0 )):
     octants.append(3)
    else:
     octants.append(-3) 

 with open('octant_input.csv', 'r') as file: # opening input file 
  reader = csv.reader(file)                     #for counting overall octants...
  l=0
  ct1=0         # counting of octant 1
  ct2=0         # counting of octant -1
  ct3=0         # counting of octant 2
  ct4=0         # counting of octant -2
  ct5=0         # counting of octant 3
  ct6=0         # counting of octant -3
  ct7=0         # counting of octant 4
  ct8=0         # counting of octant -4	 
  for l in range(rows):     #   using loop to get the octant
   if (l<rows-1):
    if (octants[l]==1):
     ct1=ct1+1
    elif(octants[l]==-1):
     ct2=ct2+1
    elif(octants[l]==2):
     ct3=ct3+1
    elif(octants[l]==-2):
     ct4=ct4+1
    elif(octants[l]==3):
     ct5=ct5+1
    elif(octants[l]==-3):
     ct6=ct6+1    
    elif(octants[l]==4):
     ct7=ct7+1
    else:
     ct8=ct8+1
    l=l+1
    # Making lists of different octants in mod range
 octants_ct1=[]      
 octants_ct2=[] 
 octants_ct3=[]     
 octants_ct4=[]
 octants_ct5=[]
 octants_ct6=[] 
 octants_ct7=[]
 octants_ct8=[] 
 with open('octant_input.csv', 'r') as file:
  reader = csv.reader(file)

  #count of octants in mod range...
  l=0
  t=0
  octs_1=0
  octs_2=0
  octs_3=0
  octs_4=0
  octs_5=0
  octs_6=0
  octs_7=0
  octs_8=0
  
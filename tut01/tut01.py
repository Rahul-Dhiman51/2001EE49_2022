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
        # calculating mean values

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

  k= int((rows-1)/mod) +1
  for l in range(k):
   y=mod*l

   for t in range(mod):	
    if(t+y<rows-1):	                                    
     if (octants[t+y]==1):
      octs_1=octs_1+1
     elif(octants[t+y]==-1):
      octs_2=octs_2+1
     elif(octants[t+y]==2):
      octs_3=octs_3+1
     elif(octants[t+y]==-2):
      octs_4=octs_4+1
     elif(octants[t+y]==3):
      octs_5=octs_5+1
     elif(octants[t+y]==-3):
      octs_6=octs_6+1    
     elif(octants[t+y]==4):
      octs_7=octs_7+1
     elif(octants[t+y]==-4):
      octs_8=octs_8+1 

   octants_ct1.append(octs_1)
   octants_ct2.append(octs_2)
   octants_ct3.append(octs_3)
   octants_ct4.append(octs_4)
   octants_ct5.append(octs_5)
   octants_ct6.append(octs_6)
   octants_ct7.append(octs_7)
   octants_ct8.append(octs_8)

   octs_1=0
   octs_2=0
   octs_3=0
   octs_4=0
   octs_5=0
   octs_6=0
   octs_7=0
   octs_8=0

 print(octants_ct1)
    #   opening output file to write...
 with open('octant_output.csv','w',newline="") as file:
  writer=csv.writer(file)
  writer.writerow(["Time",'U','V','W','Uavg','Vavg','Wavg',"U'=U-Uavg","V'=V-Vavg","W'=W-Wavg","Octant","","OctantID","+1","-1","+2","-2","+3","-3","+4","-4"])
  t=0

  for x in range(rows-1):
   if(x==0):
    writer.writerow([d1[x],a1[x],b1[x],c1[x],a_mean_value,b_mean_value,c_mean_value,a2[x],b2[x],c2[x],octants[x],"","Overall count",ct1,ct2,ct3,ct4,ct5,ct6,ct7,ct8])
   
   elif(x==1):
    y="mod "+str(mod)		
    writer.writerow([d1[x],a1[x],b1[x],c1[x],"","","",a2[x],b2[x],c2[x],octants[x],"User input",y,"","","","","","","",""])
   
   elif(x>=2 and x<2+k):
    

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
 oct = []   # declaring list for octant storing
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


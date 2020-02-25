"""
Given Two Excel Files, We want to compare the values of each column row-wise after 
sorting the values and print the changed column name and row number and values change.

"""
  
import pandas as pd 
  
sheet1 = pd.read_excel([placeholder]) 
sheet2 = pd.read_excel([placeholder]) 
  

for i,j in zip(sheet1,sheet2): # Iterating the Columns Names of both Sheets 
   
    a,b =[],[] # Creating empty lists to append the columns values    
    for m, n in zip(sheet1[i],sheet2[j]):  # Iterating the columns values 
        a.append(m) 
        b.append(n) 
 
    a.sort() 
    b.sort() 
  
    for m, n in zip(range(len(a)), range(len(b))):     # Iterating the list's values and comparing them 
        if a[m] != b[n]: 
            print('Column name : \'{}\' and Row Number : {}'.format(i,m)) 

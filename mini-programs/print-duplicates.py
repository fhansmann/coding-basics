# Python program to print  duplicates from a list of integers

def Repeat(x): 
    size = len(x) 
    repeated = []
    i = 0
    
    for i in range(size): 
        k = i + 1
        for j in range(k, size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i])
                
    return repeated 
 
input = [10, 20, 30, 20, 20, 30, 40,  
         50, -20, 60, 60, -20, -20]
         
print(Repeat(input)) 
      

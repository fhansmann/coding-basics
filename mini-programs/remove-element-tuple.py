
# Remove particular element from tuple list 
# Using list comprehension 
  
test_list = [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)] 
print("The original list is: " + str(test_list)) 
  
n = 6 
res = [tuple(ele for ele in sub if ele != n) for sub in test_list] 
print("The Tuple List after removal of element : " + str(res)) 

"""
Output:
The original list is : [(5, 6, 7), (7, 2, 4, 6), (6, 6, 7), (6, 10, 8)]
The Tuple List after removal of element : [(5, 7), (7, 2, 4), (7, ), (10, 8)]
"""

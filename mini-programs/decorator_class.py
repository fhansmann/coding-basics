
# Python program showing class decorator with return satement 
  
class SquareDecorator: 
  
    def __init__(self, function): 
        self.function = function 
  
    def __call__(self, *args, **kwargs): 
  
        # before function 
        result = self.function(*args, **kwargs) 
  
        # after function 
        return result 
  
 # adding decorator to the class 
@SquareDecorator
def get_square(n): 
    print("given number is:", n) 
    return n * n 
  
print("Square of number is:", get_square(195)) 

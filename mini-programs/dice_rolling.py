#Version A
import random 
 
def castDie():
 
   input('Press any key to cast the die!')
   r = list(range(1, 7))
   print('Result: ' + str(random.choice(r)))
 
 
while True:
   castDie()
   
   
 #Version B
 
 import random
 
def question():
        input('Press enter to roll!')
 
def roll():
    n = [1, 2, 3, 4, 5, 6]
    print(random.choice(n))
 
question()
roll()

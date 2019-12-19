#Program 1: Get a list of numbers as input from a user and calculate the sum of it

x = input("Enter a list numbers separated by space: ") #string input
userList = x.split() #separate white spaces
print("user list is ", userList)

print("Calculating sum of elements")
sum = 0
for i in userList:
    sum += int(i)
print("Sum = ", sum)
__

#Program 2: Get a list of numbers as input from a user and Print it without using a split() function

numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)

_

#Program 3: Using list Comprehension

n = int(input("Enter the size of list : "))
numList = list(int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
print("New List: ", numList)


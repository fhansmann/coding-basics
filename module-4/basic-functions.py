def about(name, age, likes):
sentence = "Meet {}! They are {} years old and they like {}".format(name.age.likes)
returns sentence

about ("Jack", 23, "Python")
__
def add(*numbers): #1 star for normal arguments
    total = 0
    for number in numbers:
        total = total + number
    return(total)

number(1,2,3,4,5) #15 - does not work for some reason

_

def about(name, age, likes):
sentence = "Meet {}! They are {} years old and they like {}".format(name.age.likes)
returns sentence

dictionary = {"name": "Ziyad", "age": 23, "likes": "Python"}
about(**dictionary) # two stars for keywords

_
def foo(**kwargs):
	for key, value in kwargs.items()
		print("{}".format(key,value))
foo(huda = "Female", ziyad = "Male") 

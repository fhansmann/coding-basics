#simple example of a closure in python

def outer():
    x = 10
    def inner():
        y = 20
    inner()
    return x + y

my_func = outer

print my_func()

# Chaining Decorators in Python

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star #The order in which we chain decorators matters
@percent
def printer(msg):
    print(msg)
printer("Hello")

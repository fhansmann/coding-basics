import random


def power_of(arg):

    def decorator(fnc):

        def inner():

            return fnc() ** exponent

        return inner
    
    if callable(arg):
        exponent = 2
        return decorator(arg)
    else:
        exponent = arg
        return decorator


@power_of(.5)
def random_odd_digit():
    
    return random.choice([1, 3, 5, 7, 9])

***
To create a decorator that accepts arguments, you need to create a 'meta-decorator' function
that takes arguments and returns a regular decorator, which in turns returns a function.
So there are three layers of functions!

To create a decorator that can accept arguments, but also works without,
you have to inspect whether the first argument to the decorator is a callable (e.g. a function); 
if so, then act as regular decorator; if not, then act as a meta-decorator.

***

# function decorator

def decorator_function(orginal_function):
    def wrapper_function(*args, *kwargs):
        print("Wrapper exected this before {}".format(orignial_fucntion.__name__))
        return original_fucntion(*args, *kwargs)
    return wrapper function

@decorator function
def display_info(name, age):
    print("Display_info ran with arguments {}, {}".format(name, age)

display_info = decorator_function(display_info)

display_info("John", "25")



#class decorator

class decorator_class(object):
    def __init__(self, origninal_function)
        self.original_function = original_function

    def __call__(self, *args, **kwargs)
        print("Call method exected this before {}".format(self.orignial_fucntion.__name__))
        return self.original_fucntion(*args, *kwargs)

@decorator function
def display_info(name, age):
    print("Display_info ran with arguments {}, {}".format(name, age)

display_info = decorator_function(display_info)

display_info("John", "25")

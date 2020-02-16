from functools import wraps


def mapper(fnc):
    
    @wraps(fnc)
    def inner(list_of_values):
        
        """This is the inner()"""
        
        return [fnc(value) for value in list_of_values]
    
    return inner


@mapper
def camelcase(s):
    
    """Turn strings_like_this into StringsLikeThis"""
    
    return ''.join([word.capitalize() for word in s.split('_')])


names = [
    'rick_ross',
    'a$ap_rocky',
    'snoop_dogg'
]

print(camelcase.__doc__) 

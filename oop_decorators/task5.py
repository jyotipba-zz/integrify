'''Write a function called double.

The function should decorate a function and return two copies of it's return value in a list.'''

def double(fnc):

    def wrapper(*args):
        lts = []
        strings = fnc(*args)
        lts.append(strings)
        return(lts*2)

    return wrapper

@double
def to_be_decorated(text):
     return text


print(to_be_decorated('Hello how are you doing ?'))

#xyz = double(to_be_decorated)
#print(xyz('string'))

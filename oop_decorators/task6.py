'''Write a function call verify. The function that is passed to this function should only
 be called if a keyword argument-value pair role:admin exists,
 otherwise the function should return "invalid" '''
from functools import wraps
def verify(fnc):

    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if key == 'role' and value == 'admin':
        #if kwargs['role']=='admin':
                strings = fnc(**kwargs)
                return strings

        return 'invalid'

    return wrapper

@verify
def check_arguments(**kwargs):
    return 'inner function called.'

if __name__ == "__main__":
    print(check_arguments(role1 = 'admin1'))

ta## Task 1

'''Write functional programming code to apply a list of functions on
a list of integers. Explain how it works
 as well and how it relates to functional programing.'''

def add(a):
     return a+a

def square(a):
    return a*a

functions = [add, square]
number = [2,3,4,5]
for num in number:
    result = map(lambda x : x(num), functions )
    print(result)

''' It is related to functional programing because
there is not change in original lists,  i.e even though
lists are mutable data type, it is made immutable. In functional
programming, we do not mutate the data, i.e change the
value of variable once it is initiated.'''

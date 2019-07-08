
'''Find the greatest common divisor of a list of numbers using Reduce.
Explain how the code works as well.
Explain how it works as well and how it relates to functional programing.'''

from math import gcd
from functools import reduce

number = [24,30, 48, 56]
greatest_comm_divi = reduce (gcd, number)
print(greatest_comm_divi)

'''
Here, gcd function from math module is used. Reduce function
takes two arguments, function and iterables. In each step, first two
item from iterables, in this case, list is passed as arguments
to gcd and  result from from it and third item from list is again applied to
function arugment in reduce. This process is continues untill
list is exhausted.

Euclidean algorithm is a algorithm to find the greatest common
divisor of two positive integer.
The Euclidean algorithm works by dividing largest integer (a) by smaller integer
 (b)and getting  get the remainder, r. If r=0, report b as the GCD of a and b.
Replace a by b and replace b by r. Return to the previous step untill
remainder is zero. The value of b when r is zero is gcd.

This is related to functional programming in a way that our original
list item is not changed in any way, i,e it is made immutable.

'''

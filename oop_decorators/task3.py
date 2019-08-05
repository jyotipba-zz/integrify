'''Task 3 (4.5 p)
Write a class that compares strings based on their length.

The class has to have such a property that we can compare different instances between each other based
on the string length without spaces.

Conditions:
Use the __new__ dunder method properly. Note that the class string objects have to be initialized
without spaces. (1.5p)
The class inherits its structure from the str class. (0.5p)
Define the Dunder methods __le__,__ge__,__lt__,__gt__,__le__ in the class that allow comparison
between class objects according to these methods. (2.5p)
'''

class StringCompare(str):

    """https://www.agiliq.com/blog/2012/06/__new__-python/"""

    def __new__(cls, content):

        new_instance = super(StringCompare, cls).__new__(cls)
        chars = ''.join( content.split())
        setattr(new_instance, 'strings', chars)
        return new_instance

    def __ge__(self, other):  ## comparing >=
        return len(self.strings) >=  len(other.strings)

    def __le__(self, other):
        return len(self.strings) <= len(other.strings)

    def __lt__(self, other):
        return len(self.strings) < len(other.strings)

    def __gt__(self, other):
          return len(self.strings) > len(other.strings)


    def __len__(self):
        return len(self.strings)

A = StringCompare("Hello how are you")
print((A.strings))

B = StringCompare('I am fine.')
print(B > A )
print(B < A )
print(B >= A )
print(B <= A )

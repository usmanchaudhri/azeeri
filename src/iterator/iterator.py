"""
Implement iterator which take 3 iterator as Input and sort it out.

- The iterable object below sets a max value initially up till where to iterate.
- It than implements the __iter__() to define the iterable variable.
- The __next__() function used the iterable variable to iterate over the values making sure the iterator does not
go beyond.
"""

class PowTwo:
    """
    Class to implement an iterator of powers of two
    """
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0  # define the iterable object

        # returns the iterable
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration()

# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get the next iterable object
print(next(i))
print(next(i))
print(next(i))
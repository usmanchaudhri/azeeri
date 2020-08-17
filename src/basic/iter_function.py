"""
Python iter() function returns an iterator function for the given object

https://www.programiz.com/python-programming/methods/built-in/iter
"""
vowels = ['a','e','i','o','u']
vowels_iter = iter(vowels)
print(next(vowels_iter))

# iter for custom objects
class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num +=1
        return self.num

print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))
print(next(print_num_iter))
print(next(print_num_iter))

# raises StopIteration
print(next(print_num_iter))

import pprint as pp
import functools
"""
On Python lambda expressions
"""

# add5 = lambda x: x+5
# print(add5(7))
#
# square = lambda x: x*x
# print(square(8))
#
# get_tens = lambda p: int(p/10)%10
# print(get_tens(749))
# print(get_tens(836.21))
#
# list1 = [('eggs', 5.25), ('honey', 9.70), ('carrots', 1.10), ('peaches', 2.45)]
# list1.sort(key = lambda x: x[0])
# print(list1)

# sort tuple using lambda function using key in tuple as the comparator
list1 = [('eggs', 5.25), ('carrot', 2.25), ('honey', 3.25), ('peaches', 4.25)]
list1.sort(key = lambda x: x[1])
pp.pprint(list1)

# lambda function on dictionary
list1 = [
    {'make': 'Ford', 'model': 'Focus', 'year': 2013},
    {'make': 'Tesla', 'model': 'X', 'year': 1999},
    {'make': 'mercedes', 'model': 'e300', 'year': 2019}]
list2 = sorted(list1, key=lambda x: x['year'])
pp.pprint(list2)

# filter a list of integers using Lambda
list1 = [1,2,3,4,5,6]
list2 = list(filter(lambda x: x%2 == 0, list1))
pp.pprint(list2)

odds = lambda x: x%2 == 1
list1 = [1,2,3,4,5,6]
list2 = list(filter(odds, list1))
pp.pprint(list2)

# using map() with lambda function
list1 = [1,2,3,4,5,6]
list2 = list(map(lambda x: x ** 2, list1))
pp.pprint(list2)

# using lambda conditionals
# lambda args: a if boolean_expression else b
starts_with_J = lambda x: True if x.startswith('J') else False
pp.pprint(starts_with_J('Joey'))

# find the word before
wordb4 = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None
sentence = 'Four score and seven years ago'
pp.pprint(wordb4(sentence, 'seven'))

# calling explicit function and calling with-in lambda
def do_something(f: callable, val: int):
    return f(val)
func = lambda x: x**3
pp.pprint(func(16))
pp.pprint(do_something(func, 5))

# reduce()
n =[4,3,2,1]
print(functools.reduce(lambda x, y: x*y), n)

def tuple():
    x = ['eggs', 3.45]
    print(x)
    print(type(x))

    x = ('eggs', 3.45)
    print(x)
    print(type(x))

    x = {'eggs', 3.45}
    print(x)
    print(type(x))

    x: dict = {'eggs': 3.45}
    x['carrot'] = 1.10
    x['potato'] = 2.34
    print(x)
    print(type(x))


# if __name__ == "__main__":
    # tuple()
import pprint as pp
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
list1.sort(key = lambda x: x[0])
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

print(float("-inf") < 0)

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
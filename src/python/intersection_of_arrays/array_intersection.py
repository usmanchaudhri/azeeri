"""

"""
def intersection(array1, array2):
    # common elements
    set1 = set(array1)
    common_elements = [element for element in array2 if element in set1]
    print(common_elements)

def intersection_1(array1, array2):
    # common elements
    common_elements = list(set(array1) & set(array2))
    print(sorted(common_elements))

array1 = [1, 2, 3, 4, 6, 7, 8]
array2 = [4, 5, 6, 7, 8, 9, 10]

# intersection(array1, array2)
intersection_1(array1, array2)
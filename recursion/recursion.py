

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)

# counter the number of items in a list recursively
def count(sequence, item):
    counter = 0                             # start the counter
    for number in sequence:
        if number == item:
            counter +=1
        elif type(number) == list:          # if element is a list it make a new search
            counter = counter + count(number, item)  # add return from search to counter
    return counter

if __name__ == "__main__":
    print(factorial(5))
    items = [1, 3, 3, [3,3,3,3], 4, 4]
    print(count(items, 3))
"""
how to create lists in python
- instantiate an empty list
- loop over an iterable or range element
- append each element to the end of the list
"""
def InstantiateEmptyList():
    squares = []
    for i in range(10):
        squares.append(i)
    print(squares)

def UsingMapObject():
    # map() provides an alternative approach that’s based in functional programming. You pass in a function and an iterable, and map() will create an object.
    txns = [1.09, 23.56, 57.84, 4.56, 6.78]
    final_prices = map(get_price_with_tax, txns)
    print(list(final_prices))

def UsingLambdaExpressions():
    # using lambda expression
    txns = [1.09, 23.56, 57.84, 4.56, 6.78]
    TAX_RATE = .08
    final_prices = map(lambda txn: txn * (1+TAX_RATE), txns)
    print(list(final_prices))

def get_price_with_tax(txn):
    TAX_RATE = .08
    return txn * (1+TAX_RATE)

def UsingListComprehensions():
    squares = [i*i for i in range(10)]
    print(squares)

def UsingListComprehensions2():
    sentence = "The rocket, who was named Ted, came back from Mars because he missed his friends."
    constants = [i for i in sentence if isConstant(i)]
    print(constants)

def isConstant(letter: str):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

def ConditionalIf():
    # new_list = [expression (if conditional) for member in iterable]
    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
    prices = [i if i > 0 else 0 for i in original_prices]
    print(prices)

def UsingSetComprehensions():
    # can create set comprehensions using curly braces
    quote = "life, uh, finds a way"
    unique_vowels = {i for i in quote if i in 'aeiou'}
    unique_vowels.remove('i')
    unique_vowels.add('p')
    print(unique_vowels)
    print(sorted(unique_vowels))

def UsingDictionaryComprehensions():
    squares = {i:i*i for i in range(10)}
    del squares[0]
    print(squares)

if __name__ == "__main__":
    # InstantiateEmptyList()
    # UsingMapObject()
    # UsingLambdaExpressions()
    # UsingListComprehensions()
    # UsingListComprehensions2()
    # ConditionalIf()
    UsingSetComprehensions()
    UsingDictionaryComprehensions()

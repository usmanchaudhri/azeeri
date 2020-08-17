"""

"""
def reverseStr(str):
    str = str[::-1]
    return str

def main():
    listOfStr = ['hi', 'this' , 'is', 'a', 'very', 'simple', 'string' , 'for', 'us']

    # reverse each string in the list
    modifiedList = list(map(reverseStr, listOfStr))
    print('Modified List', modifiedList)

    # use map function with lambda
    modifiedList = list(map(lambda x: x[::-1], listOfStr))
    print('Modified List Using Lambda', modifiedList)

    # increment ascii value of each character by 1 in the string
    sampleString = "this is a secret text"
    encryptedString = ''.join(map(lambda x: chr(ord(x) + 1), sampleString))
    print('Encrypted String using lambda and chr', encryptedString)

    print(ord('a'))
    print(ord('b'))
    print(ord('c'))

    print(chr(97))
    print(chr(98))
    print(chr(99))

    # join contents of two strings using map()
    # name = ['u', 's', 'm', 'a', 'n']
    # result = ''.join(name)

    list1 = ['hi', 'this' , 'is', 'a', 'very', 'simple', 'string' , 'for', 'us']
    list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    modifiedList = list(map(lambda x, y: x + '_' + str(y), list1, list2))
    print('Modified List', modifiedList)


    # transform all the values of a dictionary using map()
    dictOfNames = {
        7:  'sam',
        8:  'john',
        9:  'mathew',
        10: 'riti',
        11: 'aadi',
        12: 'sachin'
    }

    print('Original Dictionary')
    print(dictOfNames)

    dictOfNames = dict(map(lambda x: (x[0], x[1] + '_'), dictOfNames.items()))

    print('Modified Dictionary')
    print(dictOfNames)

    sortedDictionary = sorted(dictOfNames.items(), key=lambda x: len(x[1]))
    sortedDictionary = sorted(dictOfNames.items(), key=lambda x: x[0])
    print(sortedDictionary)


main()

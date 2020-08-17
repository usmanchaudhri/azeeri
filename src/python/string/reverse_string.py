
def reverseString(str):
    str = str[::-1]
    return str

word = "using"
listOfStr = ['hi', 'this' , 'is', 'a', 'very', 'simple', 'string' , 'for', 'us']
modifiedList = list(map(reverseString, listOfStr))
print(modifiedList)
# print(s[1:3])
# print(word[::-1])




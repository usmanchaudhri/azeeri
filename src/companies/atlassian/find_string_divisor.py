
def findStringDivisor(string, substr):
    res = string.replace(substr, '')
    if res is None:
        # find smallest string in substr
        for i in range(len(substr) - 1):
            substr[i]
            print(res)

def findRepeatStr(string, substr):
    # take all possible substrings and check it
    # with all other substrings to know if they match
    # bcdbcd
    # "b" compare to ""
    # "bc" compare to ""
    # "bcd" compare to ""
    if len(string) % len(substr):
        return -1

    # for i in range(len(substr) < len(string)):
    for i in range(1, len(substr)):
        currStr = ""          # start from the 1 which is the smallest substring exclude the empty string ""
        while len(currStr) < len(t):
            currStr = currStr + string[0:i]

        if currStr == substr:
            print("Current string %s", currStr)
            print(i)

def usingSliceAndFind(string: str):
    print("The original string : ", string)
    res = None
    temp = (string + string).find(string, 1, -1)
    if temp != -1:
        res = string[:temp]
    print("The root substring of string : " + res)

if __name__ == "__main__":
    s = "bcdbcdbcdbcd"
    t = "bcdbcd"
    # findStringDivisor(s, t)
    # findRepeatStr(s, t)
    # usingSliceAndFind(s)
    # s.replace(t, '')
    # print(s)

    print(t[4])
    print(t[0:4])
    print(t[4:])
    print(t[:4])
    print(10%1)

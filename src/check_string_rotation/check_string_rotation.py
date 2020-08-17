def areRotations(string1, string2):
    if len(string1) != len(string2):
        return 0
    temp = string1 * 2
    if temp.find(string2) != -1:
        return True
    return False

if __name__ == "__main__":
    stringA = "AACD"
    stringB = "ACDAE"
    print(areRotations(stringA, stringB))

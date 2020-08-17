"""
This was marked as easy in HackerRank
"""

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    counter = 0
    if not isOneUpperCase(password): counter +=1
    if not isOneLowerCase(password): counter +=1
    if not isSpecialCharacter(password): counter +=1
    if not isNumeric(password): counter +=1

    # if passsword is already greater tha 6
    if isMinLength(password):
        return counter
    else:
        # if password is small than 6
        missing = 6 - len(password)
        return max(missing, counter)

# if password is greater than 6 and missing charaters
# if password is smaller than 6 and missing characters
# if password is equal to 6 and missing characters

def isMinLength(password):
    return len(password) >= 6

def isOneUpperCase(password):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in password:
        if letter in upper_case:
            return True
    return False

def isOneLowerCase(password):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    for letter in password:
        if letter in lower_case:
            return True
    return False

def isSpecialCharacter(password):
    special_characters = "!@#$%^&*()-+"
    for letter in password:
        if letter in special_characters:
            return True
    return False

def isNumeric(password):
    numbers = "0123456789"
    for letter in password:
        if letter in numbers:
            return True
    return False


# word = "#HackerRank"
word = "Ab1"
minimumNumber(len(word), word)
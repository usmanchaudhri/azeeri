"""
Given a string “110010000”. Remove “100” in a recursive till the final string is empty. If not empty return false.

Example:

“110010000”->”110000”->”100”->””->empty. Return true.
“10010011”->”10011”->”11”-> notEmpty. Return false.

Questions:
- will the string only have 1's and 0's ?
"""
import re

def remove(string: str, sub_str: str):

    # base case
    if string is '':
        return True

    startIdx = string.find(sub_str)
    if startIdx is not -1:
        string = string[0: startIdx] + string[startIdx + len(sub_str): :]
    else:
        return False

    # save the return value when recursion iterates through the stack
    value = remove(string, sub_str)
    return value

if __name__ == "__main__":
    string = "110010000"
    print(remove(string, "1001"))

    # reduce_by(string, "", 0, 0, 0)
    # index = string.find("100")
    # if index == 1:
    #     string = string[0: index: ] + string[index+3: :]
    # index = string.find("100")
    # if index == 1:
    #     string = string[0: index: ] + string[index+3: :]
    # index = string.find("100")
    # if index == 1:
    #     string = string[0: index: ] + string[index+3: :]
    # if not string:
    #     print('True')
    # else:
    #     print('False')

    new_str = "100"
    idx = new_str.find("200")
    if idx is not -1:
        print("True")




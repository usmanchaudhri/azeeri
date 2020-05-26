# order of the output string does not matter
string = "uusman cchaudhri"
print("".join(set(string)))

# order of the output string matters
print("".join(dict.fromkeys(string)))


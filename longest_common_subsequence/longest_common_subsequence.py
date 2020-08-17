"""
Longest common subsequence

Given two strings find the longest common subsequence
"""

def longest_common_subsequence(str1, str2):
    lcs = [[[] for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            a = str2[i-1]
            b = str1[j-1]
            if a == b:
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)

    return lcs[-1][-1]

string1 = "ZXVVYZW"
string2 = "XKYKZPW"
lcs = longest_common_subsequence(string1, string2)
print(lcs)
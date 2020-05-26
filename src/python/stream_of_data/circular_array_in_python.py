"""
circular array in python
"""

def prints(array, n, index):
    currIdx = index
    while currIdx < n + index:  # 6+3 = 9
        # currIdx = 3, n = 6 + 3 . 3 % 6 => 3
        # currIdx = 4, n = 6 + 3 . 4 % 6 => 4
        # currIdx = 5, n = 6 + 3 . 5 % 6 => 5
        # currIdx = 6, n = 6 + 3 . 6 % 6 => 0
        # currIdx = 7, n = 6 + 3 . 7 % 6 => 1
        # currIdx = 8, n = 6 + 3 . 8 % 6 => 2
        # currIdx = 9, n = 6 + 3 . 9 % 6 => 3
        print(array[(currIdx % n)], end=' ')
        currIdx += 1

a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a);
prints(a, n, 3);

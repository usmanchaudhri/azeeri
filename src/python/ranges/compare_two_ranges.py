

# when comparing two ranges for overlap check when they don't
def isOverlap(range1, range2):
    return (not range1[1] < range2[0]) and (not range1[0] > range2[1])

if __name__== "__main__":
    print(isOverlap([17, 19], [23, 25]))
    print(isOverlap([17, 24], [23, 25]))
    print(isOverlap([17, 50], [23, 25]))

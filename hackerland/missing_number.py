"""
missing number -

Two lists are permutations of some numbers. The second list have some numbers missing, find out which numbers from list2
are missing which are there in list1. list2 is a subset of list1

"""

def find_missing(lst1, lst2):
    for ele in lst1:
        lst2.remove(ele)
    lst2.sort()
    return lst2

def read():
    f = open("missing_number_data.txt", "r")
    f.readline()
    lst1 = f.readline()
    f.readline()
    lst2 = f.readline()

    return list(lst1.split(' ')), list(lst2.split(' '))

if __name__ == "__main__":
    lst1 = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
    lst2 = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204, 100]

    from collections import defaultdict
    numDict = defaultdict(int)

    for i in range(len(lst1)):
        numDict[lst1[i]] +=1

    for i in range(len(lst2)):
        numDict[lst2[i]] -=1

    lst = []
    for key, value in numDict.items():
        if value != 0:
            lst.append(key)
    print(lst)

    # lst1, lst2 = read()
    # res = find_missing(lst1, lst2)
    # print(res)
    # print(lst1.remove(10000))


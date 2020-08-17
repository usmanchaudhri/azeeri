

def partition(array, low, high):
    i = (low - 1)           # index of smaller element
    pivot = array[high]     # pivot

    for j in range(low, high):
        # if current element if smaller than the pivot
        if array[j] < pivot:
            # increment index of smaller element
            i = i+1




if __name__ == "__main__":
    print('')
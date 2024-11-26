#  vanilla quicksort
import random

def quicksort(arr):
    if (len(arr) < 2):
        return arr
    pivot = arr[0]
    low = []; same = []; high = []
    for a in arr:
        if (a < pivot):
            low.append(a)
        elif (a > pivot):
            high.append(a)
        else:
            same.append(a)
    return quicksort(low) + same + quicksort(high)


if (__name__ == "__main__"):
    arr = [random.randint(0,999) for i in range(60)]
    print(arr)
    print()
    print(quicksort(arr))


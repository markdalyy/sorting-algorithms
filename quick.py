import random


# in-place quicksort
def _quicksort(ls, pivot, end):
    if end > pivot:
        pivotVal = ls[pivot]
        searchFpivot = pivot + 1  # search from pivot
        searchFend = end  # search from end
        while searchFpivot <= searchFend:
            while searchFpivot <= searchFend and ls[searchFpivot] < pivotVal:
                searchFpivot += 1
            while searchFpivot <= searchFend and ls[searchFend] > pivotVal:
                searchFend -= 1
            if searchFpivot <= searchFend:
                ls[searchFpivot], ls[searchFend] = ls[searchFend], ls[searchFpivot]
                searchFpivot += 1
                searchFend -= 1
            # ls[searchFend] and everything to its left is now less than the pivotVal
            # everything to its right is greater than the pivotVal
            # so swap it with the pivot
        ls[searchFend], ls[pivot] = ls[pivot], ls[searchFend]
        oldPivot = searchFend
        newPivot = pivot
        # quicksort(ls, small, pivot) --- left sublist
        _quicksort(ls, newPivot, oldPivot)
        # quicksort(ls, pivot + 1, end) --- right sublist
        _quicksort(ls, oldPivot + 1, end)


def quicksort(ls):
    n = len(ls)
    for i in range(n):
        j = random.randint(0, n - 1)
        ls[i], ls[j] = ls[j], ls[i]
    _quicksort(ls, 0, n - 1)

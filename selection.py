def selection_sort(mylist):
    n = len(mylist)
    i = 0
    while i < n:
        smallest = i
        j = i+1
        while j < n:
            if mylist[j] < mylist[smallest]:
                smallest = j
            j += 1
        mylist[i], mylist[smallest] = mylist[smallest], mylist[i]
        i += 1

# in-place insertion sort

def insertionsort(mylist):
    n = len(mylist)
    i=1
    # print(mylist, ': start by leaving', mylist[0], 'in place')
    while i < n:
        temp = mylist[i]
        j = i-1
        while temp < mylist[j] and j > -1:
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j+1] = temp
        # print(mylist, ': after inserting', temp)
        i += 1

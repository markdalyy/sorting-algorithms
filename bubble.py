def bubble_sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1], mylist[j]
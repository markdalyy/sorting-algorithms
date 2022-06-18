import math

# in-place heapsort
def heapsort(inlist):
    length = len(inlist)
    numleaves = math.ceil(length / 2)
    j = length - 1 - numleaves
    last = length - 1
    while j > -1:
        bubbledown(inlist, j, last)
        j -= 1
    for i in range(length):
        # elt to be moved up (i.e. swapped with max elt) is in position len(list)-1 - i
        # max elt being shifted is in position 0, and is going to len(list)-1-i
        # so start by swapping them, and then bubbling down the new elt in pos 0
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length - 2 - i)


def bubbledown(inlist, i, last):
    """ Bubble down item currently in pos i in a max heap. """
    while last > (i * 2):  # so at least one child
        lc = i * 2 + 1
        rc = i * 2 + 2
        maxc = lc  # start by assuming left child is the max child
        if last > lc and inlist[rc] > inlist[lc]:  # rc exists and is bigger
            maxc = rc
        if inlist[i] < inlist[maxc]:
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last

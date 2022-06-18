def linearSearch(ls, data):
    found = False
    for item in ls:
        if item[0] == data:
            found = True
            break
    return found, 'Found at position', ls.index(item)

def binarySearch(ls, data):
    # 1. Keep track of two variables, First and Last (index)
    # these are incremented/decremented to limit the part of the list to be searched
    first = 0
    last = len(ls) - 1
    found = False

    while found is False:
        # 2. Find the middle element of the list:
        mid = (first + last) // 2  # math.floor((first + last) / 2)
        # 3. Compare the middle element with the value to be found
        # If match found you're finished.
        if ls[mid][0] == data:
            found = True
        else:
            # 4. Check if the middle element is greater than the value to be found
            if ls[mid][0] > data:
                # 5. If yes, the element must lie on the first half of the list
                # Update last
                last = mid - 1
            else:
                # 6. else the element must lie on the second half of the list
                # Update first
                first = mid + 1
            if first > last:
                # not possible
                # the number doesn't exist, we've checked everything
                break
    return found

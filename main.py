# binary search is a divide and conquer algorithm
# works faster for an ordered list

# implementation of binary search
# prove that binary search is faster than naive search

# naive search: scan an entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1

def naive_search(l, target):
    # l = [1,3,10,12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# leverage the fact that the list is SORTED

def binary_search(l, target):
    # l = [1,3,5,10,12] # should return 3
    midpoint = len(l) // 2 # approx calculation of the midpoint

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target)



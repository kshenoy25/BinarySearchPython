import random
import time


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

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1
    # l = [1,3,5,10,12] # should return 3
    midpoint = (low + high) // 2 # approx calculation of the midpoint

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > ;[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':

    #l = [1,3,5,10,12]
    #target = 10
    #print(naive_search(l, target))
    #print(binary_search(l, target))

    length = 5000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    # running naive search 10000 times
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: " , (end - start)/length, "seconds")

    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: " , (end - start)/length, "seconds")
# Time complexities:
# Best case -> O(nlog(n))
# Average case -> O(nlog(n))
# Worst case -> O(nlog(n))

from math import ceil
from merge import merge

numbs = [int(i) for i in input().split(' ')]

def merge_sort(numbs: list) -> list:
    """
    Find the midpoint of the array and divide it into
    two subarrays. This is repeated until the subarrays
    have all length = 1. After the array has been
    divided, apply the merge algorithm on the subarrays
    in order to obtain a final sorted array (without
    duplicates)

    Args:
        numbs (list): The array to be sorted

    Returns:
        (list): The sorted array
    """
    if len(numbs) < 2: 
        return numbs
  
    mid = ceil(len(numbs) / 2)
    left = merge_sort(numbs[:mid]) 
    right = merge_sort(numbs[mid:]) 
  
    return merge(left, right)

# Test with user input
print(merge_sort(numbs))

# Tests without user input
assert merge_sort([5,2,7,4,1]) == [1,2,4,5,7]
assert merge_sort([10,1,4,6,2]) == [1,2,4,6,10]
assert merge_sort([5,2,9,1,4]) == [1,2,4,5,9]
assert merge_sort([7,6,4,3,2,1]) == [1,2,3,4,6,7]

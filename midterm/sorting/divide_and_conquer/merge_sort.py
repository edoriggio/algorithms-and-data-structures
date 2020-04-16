# Time complexities:
# Best case -> O(nlog(n))
# Average case -> O(nlog(n))
# Worst case -> O(nlog(n))

from math import ceil
from merge import merge

numbs = [int(i) for i in input().split(' ')]

def merge_sort(numbs: list) -> list:
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
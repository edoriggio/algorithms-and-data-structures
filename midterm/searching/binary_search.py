# Time complexities:
# Best case -> O(n) -> When the array is already sorted
# Average case -> O(n^2)
# Worst case -> O(n^2)

from math import ceil

numbs = [int(i) for i in input().split(' ')]
to_find = int(input())

def binary_search(numbs: list, to_find: int) -> bool:
    while len(numbs) > 0:
        mid = ceil(len(numbs) / 2) - 1

        if to_find < numbs[mid]:
            numbs = numbs[:mid]
        elif to_find > numbs[mid]:
            numbs = numbs[mid+1:]
        else:
            return True
    else:
        return False

# Test with user input
print(binary_search(numbs, to_find))

# Tests without user input
assert binary_search([1,2,3,4,5], 5) == True
assert binary_search([2,4,6,8,10], 2) == True
assert binary_search([-1,-2,1,2,3], 1) == True
assert binary_search([1,3,5,6,8,9], 20) == False

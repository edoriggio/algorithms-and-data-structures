# Time complexities:
# Best case -> O(n)
# Average case -> O(n)
# Worst case -> O(n)

numbs = [int(i) for i in input().split(' ')]

def partition(numbs: list) -> list:
    """
    Go through the array from left to right. If the number in
    position i is bigger than the pivot (i.e. the last number
    of the array) and the number in position j is smaller than
    or equal to the pivot, then swap the two numbers and increase
    i by one. When the end - 1 is reached, then swap the number
    in position i with the pivot.

    Args:
        numbs (list): The array to perform the partition on

    Returns:
        (list): The partitioned array
    """
    i = 0
    numb = len(numbs) - 1

    for j in range(1, len(numbs)-1):
        if numbs[i] > numbs[numb] and numbs[j] <= numbs[numb]:
            numbs[i], numbs[j] = numbs[j], numbs[i]
            i += 1
    
    numbs[numb], numbs[i] = numbs[i], numbs[numb]

    return numbs

# Test with user input
print(partition(numbs))

# Tests without user input
assert partition([5,2,7,4,1]) == [1,2,7,4,5]
assert partition([10,1,4,6,2]) == [1,2,4,6,10]
assert partition([5,2,9,1,4]) == [2,1,4,5,9]
assert partition([7,6,4,3,2,1]) == [1,6,4,3,2,7]

# Time complexities:
# Best case -> O(n^2)
# Average case -> O(n^2)
# Worst case -> O(n^2)

numbs = [int(i) for i in input().split(' ')]

def selection_sort(numbs: list):
    """
    Go through the list from left to right and serarch for the
    maximum. Once the maximum is found, swap it with the
    element at the end of the array. Repeat the same procedure
    on the subarray that goes from the beginning to the maximum
    (excluded), until the array is sorted (i.e. when the subarray
    is composed of only one element).

    Args:
        numbs (list): the array to be sorted
    
    Returns:
        (list) The sorted array
    """
    j = len(numbs) - 1
    
    while j != 0:
        i = 0
        maximum = 0

        for index, numb in enumerate(numbs[:j+1]):
            if numb >= maximum:
                maximum = numb
                i = index

        numbs[i], numbs[j] = numbs[j], numbs[i]
        j -= 1

    return numbs

# Test with user input
print(selection_sort(numbs))

# Tests without user input
assert selection_sort([5,2,7,4,1]) == [1,2,4,5,7]
assert selection_sort([10,1,4,6,2]) == [1,2,4,6,10]
assert selection_sort([5,2,9,1,4]) == [1,2,4,5,9]
assert selection_sort([7,6,4,3,2,1]) == [1,2,3,4,6,7]

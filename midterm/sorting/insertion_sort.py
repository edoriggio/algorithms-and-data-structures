# Time complexities:
# Best case -> O(n) -> When the list is already sorted
# Average case -> O(n^2)
# Worst case -> O(n^2) -> When the list is in reverse order

numbs = [int(i) for i in input().split(' ')]

def insertion_sort(numbs: list):
    """
    Go through the array from left to right. If the number in
    the i-th position is samller than the number before it,
    swap the two numbers. Repeat the same procedure until
    the array is sorted (i.e. when the end of the array is
    reached).

    Args:
        numbs (list): the array to be sorted
    
    Returns:
        (list) The sorted array
    """
    for i in range(len(numbs)):
        temp = i
        j = i - 1
        
        while j >= 0:
            if numbs[temp] < numbs[j]:
                numbs[j], numbs[temp] = numbs[temp], numbs[j]
                temp -= 1
            
            j -= 1

    return numbs

# Test with user input
print(insertion_sort(numbs))

# Tests without user input
assert insertion_sort([5,2,7,4,1]) == [1,2,4,5,7]
assert insertion_sort([10,1,4,6,2]) == [1,2,4,6,10]
assert insertion_sort([5,2,9,1,4]) == [1,2,4,5,9]
assert insertion_sort([7,6,4,3,2,1]) == [1,2,3,4,6,7]
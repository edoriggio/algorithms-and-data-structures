numbs1 = [int(i) for i in input().split(' ')]
numbs2 = [int(i) for i in input().split(' ')]

def merge(numbs1: list, numbs2: list) -> list:
    """
    Go through the two sorted arrays simultaneously from
    left to right. Find the smallest element between the 
    two in the two arrays. Append the smallest element 
    to a third array and increase the index from which the
    element was taken by one. If the two elements are the
    same, then add one of them to the third array and
    increase both indexes by one. The process is repeated 
    until the end of both arrays. If one of the two arrays
    is bigger, then add the remaining elements of the biggest
    array at the end of the iterations.

    Args:
        numbs1 (list): The first array to be merged
        numbs2 (list): The second array to be merged

    Returns:
        (list) The sorted array
    """
    sorted_numbs = []
    i = j = 0

    while i < len(numbs1) and j < len(numbs2):
        if numbs1[i] < numbs2[j]:
            sorted_numbs.append(numbs1[i])
            i += 1
        elif numbs2[j] < numbs1[i]:
            sorted_numbs.append(numbs2[j])
            j += 1
        else:
            sorted_numbs.append(numbs1[i])
            i += 1
            j += 1

    if i < len(numbs1):
        sorted_numbs += numbs1[i:]
    
    if j < len(numbs2):
        sorted_numbs += numbs2[j:]

    return sorted_numbs

# Test with user input
print(merge(numbs1, numbs2))

# Tests without user input
assert merge([1,3,5,7,9], [2,4,6,8,10]) == [1,2,3,4,5,6,7,8,9,10]
assert merge([2,5,7], [1,6,7,13,15]) == [1,2,5,6,7,13,15]
assert merge([1,2,6,8,9,12], [1,5,7,8]) == [1,2,5,6,7,8,9,12]
assert merge([1,2,6,8,9,12], []) == [1,2,6,8,9,12]
assert merge([], [1,5,7,8]) == [1,5,7,8]

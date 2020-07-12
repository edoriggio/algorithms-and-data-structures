# Copyright 2020 Edoardo Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Time complexities:
# Best case -> O(nlog(n))
# Average case -> O(nlog(n))
# Worst case -> O(n^2)

numbs = [int(i) for i in input().split(' ')]

def partition(numbs: list, low: int, high: int) -> int:
    """
    Go through the array from left to right. If the number in
    position i is bigger than the pivot (i.e. the last number
    of the array) and the number in position j is smaller than
    or equal to the pivot, then swap the two numbers and increase
    i by one. When the end is reached, then swap the number
    in position i + 1 with the pivot and make i + 1 the pivot.

    Args:
        numbs (list): The array to be sorted
        low (int): The beginning of the subarray
        high (int): The end of the subarray

    Returns:
        (int): The index of the pivot
    """
    i = low - 1
    pivot = numbs[high]

    for j in range(low, high):
        if numbs[j] <= pivot:
            i += 1
            numbs[i], numbs[j] = numbs[j], numbs[i]

    numbs[high], numbs[i+1] = numbs[i+1], numbs[high]
    pivot = i + 1

    return pivot

def quick_sort(numbs: list, low: int, high: int) -> list:
    """
    If the index low is less than the index high, then
    partition the array. The process is repeated for the
    right part of the array (i.e. numbs[pi+1:]) and the
    left part of the array (i.e. numbs[:pi-1]). The
    algorithm will stop when the array is sorted.

    Args:
        numbs (list): The array to be sorted
        low (int): The beginning of the subarray
        high (int): The end of the subarray

    Returns:
        (list): The sorted array
    """
    if low < high: 
        pi = partition(numbs, low, high) 
  
        quick_sort(numbs, low, pi-1) 
        quick_sort(numbs, pi+1, high)

    return numbs

# Test with user input
print(quick_sort(numbs, 0, len(numbs)-1))

# Tests without user input
assert quick_sort([5,2,7,4,1], 0, len([5,2,7,4,1])-1) == [1,2,4,5,7]
assert quick_sort([10,1,4,6,2], 0, len([10,1,4,6,2])-1) == [1,2,4,6,10]
assert quick_sort([5,2,9,1,4], 0, len([5,2,9,1,4])-1) == [1,2,4,5,9]
assert quick_sort([7,6,4,3,2,1], 0, len([7,6,4,3,2,1])-1) == [1,2,3,4,6,7]

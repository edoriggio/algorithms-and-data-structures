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
# Best case -> O(n) -> When the array is already sorted
# Average case -> O(n^2)
# Worst case -> O(n^2)

numbs = [int(i) for i in input().split(' ')]

def bubble_sort(numbs: list) -> list:
    """
    Go through the array from left to right, for each couple of
    numbers, check which one is bigger. If the first element of
    the couple is bigger than the second, swap the two numbers.
    Repeat the same process until the array is sorted (i.e.
    when the number of swaps is equal to 0).

    Args:
        numbs (list): The array to be sorted
    
    Returns:
        (list) The sorted array
    """
    while True:
        changes = 0

        for index in range(len(numbs)-1):
            if numbs[index] > numbs[index+1]:
                numbs[index], numbs[index+1] = numbs[index+1], numbs[index]
                changes += 1
        
        if changes == 0:
            return numbs

# Test with user input
print(bubble_sort(numbs))

# Tests without user input
assert bubble_sort([5,2,7,4,1]) == [1,2,4,5,7]
assert bubble_sort([10,1,4,6,2]) == [1,2,4,6,10]
assert bubble_sort([5,2,9,1,4]) == [1,2,4,5,9]
assert bubble_sort([7,6,4,3,2,1]) == [1,2,3,4,6,7]

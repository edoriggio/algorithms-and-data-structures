# Time complexities:
# Best case -> O(n) -> When the list is already sorted
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

# Average case -> O(n^2)
# Worst case -> O(n^2) -> When the list is in reverse order

numbs = [int(i) for i in input().split(' ')]

def insertion_sort(numbs: list) -> list:
    """
    Go through the array from left to right. If the number in
    the i-th position is samller than the number before it,
    swap the two numbers. Repeat the same procedure until
    the array is sorted (i.e. when the end of the array is
    reached).

    Args:
        numbs (list): The array to be sorted
    
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

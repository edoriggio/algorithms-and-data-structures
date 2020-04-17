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
# Best case -> O(1) -> When the number to be found is the first
# Average case -> O(n)
# Worst case -> O(n)

numbs = [int(i) for i in input().split(' ')]
to_find = int(input())

def linear_search(numbs: list, to_find: int) -> bool:
    """
    Go through the array from left to right. If the number
    of the array is equal to the number to_find, then return
    true. If after the for loop the number has not been found,
    return false

    Args:
        numbs (list): The array to be sorted
        to_find (int): The element to be found in the array

    Returns:
        (bool) True if the element is in the array
               False if the element is not in the array
    """
    for i in numbs:
        if i == to_find:
            return True
    else:
        return False

# Test with user input
print(linear_search(numbs, to_find))

# Tests without user input
assert linear_search([1,2,3,4,5], 5) == True
assert linear_search([2,4,6,8,10], 2) == True
assert linear_search([-1,-2,1,2,3], 1) == True
assert linear_search([1,3,5,6,8,9], 20) == False
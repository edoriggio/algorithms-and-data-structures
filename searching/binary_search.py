# Time complexities:
# Copyright 2021 Edoardo Riggio
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
# Best case -> O(1) -> When the number to be found is equal to mid
# Average case -> O(log(n))
# Worst case -> O(log(n))

from math import ceil


def binary_search(numbs: list, to_find: int):
    """
    Get the element in the middle of a sorted array. If the number
    to find is greater than the mid, then let the right subarray be
    the new array and repeat the first step here. Otherwise repeat
    the first step on the left subarray. If the value to find is
    equal to the mid, then return true. If the element is not found
    (i.e. the array's length is 0), then return false.

    Args:
        numbs (list): The array to be sorted
        to_find (int): The element to be found in the array

    Returns:
        (bool) True if the element is in the array
               False if the element is not in the array
    """
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


print(binary_search([1, 2, 3, 4, 5], 5))

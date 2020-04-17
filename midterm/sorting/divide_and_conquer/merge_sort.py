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
# Worst case -> O(nlog(n))

from math import ceil
from merge import merge

numbs = [int(i) for i in input().split(' ')]

def merge_sort(numbs: list) -> list:
    """
    Find the midpoint of the array and divide it into
    two subarrays. This is repeated until the subarrays
    have all length = 1. After the array has been
    divided, apply the merge algorithm on the subarrays
    in order to obtain a final sorted array (without
    duplicates)

    Args:
        numbs (list): The array to be sorted

    Returns:
        (list): The sorted array
    """
    if len(numbs) < 2: 
        return numbs
  
    mid = ceil(len(numbs) / 2)
    left = merge_sort(numbs[:mid]) 
    right = merge_sort(numbs[mid:]) 
    
    # Merge algorithm is the same as /midterm/misc/merge.py
    return merge(left, right)

# Test with user input
print(merge_sort(numbs))

# Tests without user input
assert merge_sort([5,2,7,4,1]) == [1,2,4,5,7]
assert merge_sort([10,1,4,6,2]) == [1,2,4,6,10]
assert merge_sort([5,2,9,1,4]) == [1,2,4,5,9]
assert merge_sort([7,6,4,3,2,1]) == [1,2,3,4,6,7]
assert merge_sort([1,5,4,2,6,7,3,21,1,9,5,8,2]) == [1,2,3,4,5,6,7,8,9,21]

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
# Best case -> O(n) -> When v is equal to to_find
# Average case -> O(nlog(n))
# Worst case -> O(nlog(n))

from random import randint

numbs = [int(i) for i in input().split(' ')]
to_find = int(input())

def selection(numbs: list, to_find: int) -> int:
    """
    Generate a random number between 0 and the length of
    the array - 1. Go through the list from left to right.
    if the number of the array is smaller than the number
    at the index of the random number, put the former in
    numbs_l, if it is bigger in numbs_r, and if it is equal
    in numbs_v. After perform a check to see if the number
    to_find is less than or equal to the length of numbs_l.
    If that is the case assign numbs_l to numbs. If it is
    greater than the lengths of numbs_l + numbs_v, then assign
    numbs_l to numbs and the lengths numbs_l + numbs_v to
    to_find. Otherwise return the number in rand. The process
    is repeated until the number is found (i.e. the else
    condition of the last if-block is satisfied).

    Args:
        numbs (list): The array from which we find the number
        to_find (int): The i-th smaller number of the array

    Returns:
        (int): The i-th smallest number of the array
    """
    if len(numbs) == 0 or to_find > len(numbs):
        return "input error"
    
    while True:
        numbs_l = []
        numbs_r = []
        numbs_v = []

        rand = randint(0, len(numbs)-1)

        for i in range(0, len(numbs)):
            if numbs[i] < numbs[rand]:
                numbs_l.append(numbs[i])
            elif numbs[i] > numbs[rand]:
                numbs_r.append(numbs[i])
            else:
                numbs_v.append(numbs[i])

        if to_find <= len(numbs_l):
            numbs = numbs_l
        elif to_find > len(numbs_l) + len(numbs_v):
            numbs = numbs_r
            to_find -= len(numbs_l) + len(numbs_v)
        else:
            return numbs[rand]

# Test with user input
print(selection(numbs, to_find))

# Tests without user input
assert selection([1,2,3,4,5,6,7,8,9,10], 1) == 1
assert selection([1,2,3,4,5,6,7,8,9,10], 2) == 2
assert selection([2,36,5,21,8,13,11,20,5,4,1], 7) == 11
assert selection([1], 1) == 1
assert selection([], 1) == "input error"
assert selection([1], 10) == "input error"

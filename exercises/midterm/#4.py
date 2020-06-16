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

# Problem:
# A left-rotation of an array A is defined as a permutation of A such that
# every element is shifted by one position to the left except for the fist
# element that is moved to the last position. For example, with
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9], a left-rotation would change A into
# A = [2, 3, 4, 5, 6, 7, 8, 9, 1].

# Complexity:
# O(n)

def rotate(array, times):
    flip(array, 0, times-1)
    flip(array, 0, len(array)-1)
    flip(array, 0, len(array)-times-1)

    return array

def flip(array, low, high):
    for i in range(low, high):
        if i <= high//2:
            array[i], array[high-i] = array[high-i], array[i]

print(rotate([2,4,5,7,8,10,11], 3))

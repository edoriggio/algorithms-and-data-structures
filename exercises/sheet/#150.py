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
# Write an algorithm Three-Way-Partition(A, v) that takes an array A of n
# numbers, and partitions A in-place in three parts, some of which might
# be empty, so that the left part A[1 ... p − 1] contains all the elements
# less than v, the middle part A[p ... q − 1] contains all the elements
# equal to v, and the right part A[q ... n] contains all the elements greater
# than v. Three-Way-Partition must return the positions p and q and must 
# run in time O(n).

# Complexity:
# O(n)

def three_way_partition(array, numb):
    i = 0
    pivot = numb
    same = 0

    for element in array:
        if array[element] == numb:
            array[element], array[-1] = array[-1], array[element] 
            break

    for j in range(1, len(array)):
        if array[j] <= array[-1]:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[-1], array[i+1] = array[i+1], array[-1]

    while i >= 0:
        if array[i] == pivot:
            i -= 1
        else:
            same = i
            break

    for numb in range(same+1):
        if same > numb:
            if array[numb] == pivot:
                array[numb], array[same] = array[same], array[numb]
                same -= 1
    
    return (same, i+2)

print(three_way_partition([1,7,1,8,8,10,2,8,40,32,11,27], 8))

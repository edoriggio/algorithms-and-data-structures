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

# Problem:
# Consider an array A of n numbers that is initially sorted, in ascending
# order, and hen modified so that k of its elements are decreased in value.
# - Question 1: Write an algorithm that sorts A in-place in time O(kn).
# 
# - Question 2: Write an algorithm that sorts A in time O(n+klogk) but
#   not necessarily in-place.

# Complexity:
# (1) - O(kn)
# (2) - O(klogk)

# (1)
def re_sort(array, elements):
    for j in elements:
        for i in range(j):
            if array[j] <= array[i]:
                array[j], array[i] = array[i], array[j]

    return array

# (2)
def re_sort_parts(array, elements):
    sorted_array = []

    for i in elements:
        sorted_array = array[:i+1]
        sorted_array.sort()

    return sorted_array

print(re_sort([1,4,2,7,8,6,10,14,3], [2,5,6,8]))
print(re_sort_parts([1,4,2,7,8,6,10,14,3], [2,5,6,8]))

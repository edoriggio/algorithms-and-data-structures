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
# Write an algorithm called Find-Largest that finds the largest number
# in an array using a divide-and-conquer strategy.

# Complexity:
# O(nlog(n))

# def partition(array, low, high):
#     i = low - 1
#     pivot = array[high]
#
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#
#     array[high], array[i+1] = array[i+1], array[high]
#     pivot = i + 1
#
#     return pivot

def find_largest(array, high, low = 0):
    if low < high: 
        part = partition(array, low, high) 
  
        find_largest(array, low, part-1) 
        find_largest(array, part+1, high)

    return array[-1]

print(find_largest([10,2,40,20,2,9,8], 6))

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
# Write an algorithm called Find-Largest that finds the largest number
# in an array using a divide-and-conquer strategy.

# Complexity:
# O(n^2)

def in_place_sel_sort(array):
    for i in range(len(array)):
        temp = i
        j = i - 1

        while j >= 0:
            if array[temp] < array[j]:
                array[temp], array[j] = array[j], array[temp]
                temp -= 1
            
            j -= 1

    return array

print(in_place_sel_sort([7,17,89,74,21,7,43,9,26,10]))

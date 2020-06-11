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
# Develop an efficient in-place algorithm called Partition-Even-Odd(A) 
# that partitions an array A in even and odd numbers. The algorithm must
# terminate with A containing all its even elements preceding all its odd
# elements. For example, for input A = [h7, 17, 74, 21, 7, 9, 26, 10], the 
# result might be A = [74, 10, 26, 17, 7, 21, 9, 7]. Partition-Even-Odd 
# must be an in-place algorithm, which means that it may use only a constant
# memory space in addition to A. In practice, this means that you may not
# use another temporary array.

# Complexity:
# O(n)

def partition_even_odd(array):

    i = 0
    j = 0
    length = len(array)

    while j < length:
        if array[i] % 2 != 0:
            array.append(array[i])
            del array[i]
        else:
            i += 1
            
        j += 1

    return array

print(partition_even_odd([7, 17, 74, 21, 7, 9, 26, 10]))

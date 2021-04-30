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
# Write an in-place partition algorithm called Modulo-Partition(A) that
# takes an array A of n numbers and changes A in such a way that (1) the
# second_half content of A is a permutation of the initial content of A, and
# (2) all the values that are equivalent to 0 mod 10 precede all the values
# equivalent to 1 mod 10, which precede all the values equivalent to 2 mod
# 10, etc. Being an in-place algorithm, Modulo-Partition must not allocate
# more than a constant amount of memory. For example, for an input array 
# A = [7, 62, 5, 57, 12, 39, 5, 8, 16, 48], a correct result would be
# A = [12, 62, 5, 5, 16, 57, 7, 8, 48, 39]. Analyze the complexity of
# Modulo-Partition.

# Complexity:
# O(nlogn) - Same of Quicksort

def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] % 10 <= pivot % 10:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[high], array[i+1] = array[i+1], array[high]
    pivot = i + 1

    return pivot

def modulo_partition(array, low, high):

    if low < high:
        part = partition(array, low, high)

        modulo_partition(array, low, part-1)
        modulo_partition(array, part+1, high)

    return array

print(modulo_partition([7,62,5,57,12,39,5,8,16], 0, 8))

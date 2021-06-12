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

# Given an array A, find the two elements that summed together gives the
# maximum result.

from math import inf


def algo_y(A):
    m = -inf

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] > m:
                m = A[i] + A[j]

    return m


def better_algo_y(A):
    max_sum = 0

    curr_max = -inf
    curr_max_ind = 0

    for i in range(len(A)):
        if A[i] > curr_max:
            curr_max = A[i]
            curr_max_ind = i

    max_sum = curr_max
    curr_max = -inf
    A[curr_max_ind] = None

    for i in range(len(A)):
        if A[i] != None and A[i] > curr_max:
            curr_max = A[i]

    max_sum += curr_max

    return max_sum
    

array = [1, 5, 3, 4, 6]
print(algo_y(array))
print(better_algo_y(array))

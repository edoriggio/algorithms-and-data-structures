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

# Complexity: O(n^4)

# This algorithm returns the beginning and the end (excluded)
# of the subarray where there are k contiguous and equal
# elements. Even if the equal numbers are more than k.

from math import inf


def algo_x(A, k):
    l = -inf
    r = inf

    # 1st for loop -> n
    for i in range(len(A)-k):

        # 2nd for loop (nested) -> n
        for j in range(i+1, len(A)):
            if algo_y(A, i, j) >= k:
                if r - l > j - i:
                    l = i
                    r = j

    return l, r


def algo_y(A, a, b):
    m = 1

    # 3rd for loop (nested) -> n
    for i in range(a, b):
        c = 1

        # 4th for loop (nested) -> n
        for j in range(i+1, b):
            if A[i] == A[j]:
                c += 1

        if c > m:
            m = c

    return m


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(n).

def better_algo_x(A, k):
    s = 0
    count = 1
    numb = A[0]

    # For loop -> n
    for i in range(1, len(A)):
        if A[i] != numb:
            if count >= k:
                return s, s+k

            s = i
            numb = A[i]
        else:
            count += 1

    return -inf, inf


arr = [4, 3, 3, 3, 3, 3, 50, 2, 3, 3, 3, 4]
print(algo_x(arr, 2))
print(better_algo_x(arr, 2))

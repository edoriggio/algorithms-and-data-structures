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

# Complexity: O(n^2)

# Return the category that has the highest total weight

from math import inf


def algo_x(A):
    c = A[0][1]
    w = -inf

    # Complexity: O(n)
    for i in range(len(A)):
        t = 0

        # Complexity: O(n)
        for j in range(len(A)):
            if A[j][1] == A[i][1]:
                t += A[j][0]

        if t > w or (t == w and c > A[i][1]):
            c = A[i][1]
            w = t

    return c


# Complexity: O(n log(n))

def better_algo_x(A):
    # Complexity: O(n log(n))
    A.sort()

    max_weight = -inf
    max_cat = A[0][0]
    curr_weight = A[0][1]

    # Complexity: O(n)
    for i in range(1, len(A)):
        if A[i-1][0] != A[i][0]:
            if curr_weight > max_weight:
                max_weight = curr_weight
                max_cat = A[i-1][0]
                curr_weight = A[i][1]
        else:
            curr_weight += A[i][1]

    if curr_weight > max_weight:
        max_weight = curr_weight
        max_cat = A[i-1][0]

    if A[-1][0] != A[-2][0] and A[-1][1] > max_weight:
        max_cat = A[-1][0]

    return max_cat


array = [(2, 3), (5, 1), (2, 4), (3, 1), (1, 4), (3, 2), (9, 12)]
print(better_algo_x(array))

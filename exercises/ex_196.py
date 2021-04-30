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

# Complexity: O(n^3)

# The worst-case scenario is when the whole array is
# in increasing order. In this case the loop in algo_y
# would always run from the beginning to the end (i.e.
# in n). The goal of this algorithm finds the increasing
# subsequence that has the biggest difference between
# the last element and the first element. It returns
# the biggest difference.

def algo_x(A):
    x = 0

    # 1st for loop -> n
    for i in range(len(A)-1):
        # 2nd for loop (nested) -> n
        for j in range(i+1, len(A)):
            if algo_y(A, i, j) and A[j] - A[i] > x:
                x = A[j] - A[i]

    return x


def algo_y(A, i, j):
    # 3rd for loop (nested) -> n
    for k in range(i, j):
        if A[k] > A[k+1]:
            return False

    return True


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(n).

def linear_algo_x(A):
    max_dist = 0
    start = 0

    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            if A[i-1] - A[start] > max_dist:
                max_dist = A[i-1] - A[start]

            start = i

    return max_dist


arr = [1, 5, 2, 4, 9, 7, 9, 3, 3, 4]
print(algo_x(arr))
print(linear_algo_x(arr))

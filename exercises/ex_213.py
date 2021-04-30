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

# This algorithm chackes if there is a subarray that
# has lenght of maximum k elements, and they all must
# be smaller than A[k].

def algo_x(A, k):
    # 1st for loop -> n
    for i in range(len(A)):
        if algo_y(A, A[i]) == k:
            return A[i]

    return None


def algo_y(A, y):
    c = 0

    # 2nd for loop (nested) -> n
    for i in range(len(A)):
        if A[i] < y:
            c += 1

    return c


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(nlog(n)).

def better_algo_x(A, k):
    # Timsort -> nlog(n)
    A.sort()

    if k < 0 or k >= len(A):
        return None

    # For loop -> k
    # k can never be greater than n, thus the maximum
    # complexity of this loop is n
    for i in range(k):
        if A[i] == A[k]:
            return None

    return A[k]


arr = [2, 5, 4, 3, 4, 7, 9, 8, 2]
arr1 = [2, 5, 4, 3, 4, 7, 9, 8, 2]
print(algo_x(arr, 5))
print(better_algo_x(arr1, 5))

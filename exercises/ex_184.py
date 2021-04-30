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

# Partition the array by having all odd numbers at the
# beginning and all even numbers at the end. It returns
# the point where the even partition begins.

def algo_x(A):
    i = 0
    j = len(A)

    # 1st while loop -> n
    while i < j:
        if A[i] % 2 == 0:
            j -= 1
            v = A[i]

            algo_y(A, i, j)

            A[j] = v
        else:
            i += 1

    print(A)
    return j


def algo_y(A, p, q):
    # 2nd while loop (nested) -> n
    while p < q:
        A[p] = A[p+1]
        p += 1


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(n).

def better_algo_x(A):
    i = 0
    j = len(A) - 1

    # While loop -> n
    while i < j:
        if A[i] % 2 == 0:
            A[j], A[i] = A[i], A[j]
            j -= 1
        else:
            i += 1

    return j


arr = [1, 2, 4, 5, 8, 7, 0, 9]
arr1 = [1, 2, 4, 5, 8, 7, 0, 9]
print(algo_x(arr))
print(better_algo_x(arr1))

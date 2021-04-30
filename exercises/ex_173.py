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

# This algorithm looks for the maximum difference
# between two elements in the array.

from math import inf


def algo_x(A):
    i = 1
    j = 0
    x = -inf

    # While loop -> n^2
    while i < len(A):
        if abs(A[i] - A[j]) > x:
            x = abs(A[i] - A[j])

        j += 1

        if j == i:
            i += 1
            j = 0

    return x


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(n).

def better_algo_x(A):
    biggest = -inf
    smallest = +inf

    # For loop -> n
    for i in range(len(A)):
        if A[i] > biggest:
            biggest = A[i]

        if A[i] < smallest:
            smallest = A[i]

    return biggest - smallest


arr = [5, 2, 6, 1, 5, 4]
print(algo_x(arr))
print(better_algo_x(arr))

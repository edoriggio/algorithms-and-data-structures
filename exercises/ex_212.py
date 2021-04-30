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

# This algorithm checks all possible couples and returns true
# if at least one pair has the absolute value of the difference
# greater than x.

from math import inf


def algo_x(A, x):
    i = len(A)-1
    j = 0

    # While loop -> n^2
    while i > 0:
        if j == i:
            j = 0
            i -= 1
        elif A[i] - A[j] > x or A[j] - A[i] > x:
            return True
        else:
            j += 1

    return False


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(n).

def better_algo_x(A, x):
    min_numb = +inf
    max_numb = -inf

    # For loop -> n
    for i in range(len(A)):
        if A[i] > max_numb:
            max_numb = A[i]

        if A[i] < min_numb:
            min_numb = A[i]

    if max_numb - min_numb > x or min_numb - max_numb > x:
        return True

    return False


arr = [1, 20, 2, 10, 9, 5, 7, 3, 5, 2, 4]
print(algo_x(arr, 18))
print(better_algo_x(arr, 18))

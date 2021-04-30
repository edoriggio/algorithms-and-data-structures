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

# Complexity: O(n_max^n)

# This algorithm multiplies every element in the array
# and returns the result of said multiplication.

def algo_x(A):
    B = list(A)
    i = 0
    x = 1

    while i < len(A):
        B[i] = B[i] - 1

        if B[i] == 0:
            B[i] = A[i]
            i += 1
        else:
            x += 1
            i = 0

    return x


# An algorithm with a stricly better worst-case
# complexity is the following. In this case the
# worst-case complexity is O(n).

def better_algo_x(A):
    prod = A[0]

    # For loop -> n
    for i in range(1, len(A)):
        prod *= A[i]

    return prod


arr = [2, 5, 9, 8]
print(algo_x(arr))
print(better_algo_x(arr))

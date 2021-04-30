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

# The wort-case scenario is represented by any A.
# The algorithm will always iterate over all of A
# in both the first for loop and in the second
# loop. The goal of this algorithm is to find the
# number that is repeated the most amount of times.

def algo_x(A):
    x = 0
    y = 0

    # 1st for loop -> n
    for i in range(len(A)):
        k = 15

        # 2nd for loop (nested) -> n
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                k += 1

                if x < k:
                    x = k
                    y = A[i]

    return y


# An algorithm with a stricly better complexity
# is the following. In this case the complexity
# is O(nlog(n)).

def better_algo_x(A):
    # Timsort -> nlog(n)
    A.sort()

    number = A[0]
    counter = 1

    max_number = A[0]
    max_counter = 1

    # For loop -> n
    for i in range(1, len(A)):
        if A[i] == number:
            counter += 1
        else:
            number = A[i]
            counter = 1

        if counter > max_counter:
            max_number = A[i]
            max_counter = counter

    return max_number


arr = [9, 5, 7, 9, 20, 50, 42, 9]
print(algo_x(arr))
print(better_algo_x(arr))

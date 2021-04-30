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

# Time complexity: O(n)
# Space complexity: O(1)

def is_good(x):
    return x % 2 == 0


def good_are_adjacent(A):
    adjacent = False
    not_good = False

    for i in range(len(A)):
        if is_good(A[i]):
            adjacent = True
        elif not is_good(A[i]) and adjacent:
            not_good = True

        if adjacent and not_good and is_good(A[i]):
            return False

    return adjacent


# Complexity: O(n)

def make_good_adjacent(A):
    i = 0
    j = len(A) - 1

    while i < j:
        if is_good(A[i]):
            A[i], A[j] = A[j], A[i]
            j -= 1
        else:
            i += 1

    return A


arr = [1, 2, 5, 2, 1, 3]
print(good_are_adjacent(arr))
print(make_good_adjacent(arr))

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

def rotate(A, k):
    if k > len(A) or k == 0:
        return A

    A = reverse(A, 0, len(A)-1)
    A = reverse(A, 0, len(A)-k-1)
    A = reverse(A, len(A)-k, len(A)-1)

    return A


def reverse(A, b, e):
    i = b
    j = e

    # While loop -> n
    while i != j:
        A[i], A[j] = A[j], A[i]

        if (i + 1 == j):
            break

        i += 1
        j -= 1

    return A


arr = [1, 2, 3, 4, 6, 7, 8, 9]
print(rotate(arr, 3))

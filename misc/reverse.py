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

def reverse(A, b, e):
    """Completely flip the given array/subarray.

    Args:
        A (array): the array to flip.
        b (int): the index of the beginning of the array/subarray
                 to flip
        e (int): the index of the end of the array/subarray to flip

    Returns:
        array: the refersed array
    """
    i = b
    j = e

    while i != j:
        A[i], A[j] = A[j], A[i]

        if (i + 1 == j):
            break

        i += 1
        j -= 1

    return A

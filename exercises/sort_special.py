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

# Complexity: O(n)

from math import inf

def sort_special(A):
    max_value = -inf
    min_value = +inf
    min_i = max_i = 0

    # For loop -> n
    for i in range(len(A)):
        if A[i] < min_value:
            min_i = i
            min_value = A[i]
        
        if A[i] > max_value:
            max_i = i
            max_value = A[i]

    A[0], A[min_i] = A[min_i], A[0]
    A[-1], A[max_i] = A[max_i], A[-1]

    if A[1] > A[2]:
        A[1], A[2] = A[2], A[1]

    print(A)


arr = [4, 4, 5, 4]
sort_special(arr)

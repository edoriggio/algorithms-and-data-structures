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

def maximal_distance(A):
    max_n = -inf
    min_n = +inf

    if len(A) < 2:
        return 0

    for i in range(len(A)):
        if A[i] < min_n:
            min_n = A[i]

        if A[i] > max_n:
            max_n = A[i]

    return max_n - min_n


arr = [2, 5, 9, 20, 1, 2, 7, 9, 10]
print(maximal_distance(arr))

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

def max_danger(A):
    max_danger = 1
    curr_danger = 1

    # Complexity: O(n)
    for i in range(1, len(A)):
        if A[i-1][2] > A[i][2] and A[i-1][1] < A[i][1]:
            curr_danger += 1
        else:
            curr_danger = 1

        max_danger = max(curr_danger, max_danger)

    if max_danger == 1:
        return 0

    return max_danger


array = [[1, 2, 10], [2, 4, 9], [3, 5, 10], [4, 6, 9], [5, 7, 6], [6, 0, 0]]
print(max_danger(array))

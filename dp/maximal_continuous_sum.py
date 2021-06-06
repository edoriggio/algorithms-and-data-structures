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

def maximal_continuous_sum(A):
    if len(A) < 1:
        return None

    dp = A[0]
    max_sum = A[0]

    for i in range(len(A)-1):
        dp = max(dp + A[i+1], A[i+1])
        max_sum = max(dp, max_sum)

    return max_sum


array = [1, 4, 2, 0, -1, -5, 9, 10, 2]
print(maximal_continuous_sum(array))

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

# Complexity O(n)

def minimal_contiguous_sum(A):
    if len(A) < 1:
        return None

    dp = A[0]
    m_sum = A[0]

    for i in range(len(A)-1):
        dp = min(dp + A[i+1], A[i+1])
        m_sum = min(dp, m_sum)

    return m_sum


array = [-1, 2, -2, -4, 1, -2, 5, -2, -3, 1, 2, -1]
print(minimal_contiguous_sum(array))

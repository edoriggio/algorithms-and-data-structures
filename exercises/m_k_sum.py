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

def m_k_sum(A, m, k):
    max_sum = A[0]
    curr_sum = A[0]
    curr_k = 1

    for i in range(len(A)-1):
        if curr_k + 1 <= k:
            if curr_k + 1 == k:
                if curr_sum + A[i+1] >= m:
                    return True
                else:
                    curr_sum = max(curr_sum, A[i+1])

                    if (curr_sum < A[i+1]):
                        curr_k = 1
                
                    max_sum = max(curr_sum, max_sum)
            else:
                curr_sum = max(curr_sum, A[i+1], curr_sum + A[i+1])

                if (A[i+1] > A[i] and A[i+1] > curr_sum + A[i+1]):
                    curr_k = 1
                elif (curr_sum + A[i+1] > A[i] and curr_sum + A[i+1] > A[i+1]):
                    curr_k += 1
                    
                max_sum = max(curr_sum, max_sum)

    if max_sum >= m:
        return True
    
    return False


array = [2, 1, 4, 1, 8, 7, 2, 4]
print(m_k_sum(array, 12, 3))

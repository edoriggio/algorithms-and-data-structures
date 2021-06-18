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

def longest_mirror_seq_2(A, B):
    x = [0] * (len(A)+1)
    DP = []

    max_seq = 0

    for _ in range(len(B)+1):
        DP.append(x[:])

    # Complexity: O(n)
    for i in range(1, len(B)+1):
        # Complexity: O(n)
        for j in range(1, len(x)):
            if A[j-1] == B[i-1] and j < len(x)-1 and DP[i-1][j+1] != 0:
                DP[i][j] = DP[i-1][j+1] + 1

                if DP[i][j] > max_seq:
                    max_seq = DP[i][j]

            elif A[j-1] == B[i-1]:
                DP[i][j] = 1

                if max_seq == 0:
                    max_seq = 1

    return max_seq


array_a = [3, 7, 4, 5, 7]
array_b = [3, 7, 5, 4, 3]
print(longest_mirror_seq_2(array_a, array_b))

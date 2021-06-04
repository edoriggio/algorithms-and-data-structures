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

# Complexity: O(n^2) - where n is the sum of the elements in values and
# max_w.

def knapsack(values, weights, max_w):
    x = [0] * (max_w + 1)
    DP = []

    for i in range(len(values)+1):
        DP.append(x[:])

    for i in range(1, max_w+1):
        for j in range(1, len(x)):
            if i-1 >= len(values):
                return DP[-1][-1]

            if j >= weights[i-1]:
                DP[i][j] = max(DP[i-1][j], values[i-1] +
                               DP[i-1][j - weights[i-1]])
            else:
                DP[i][j] = DP[i-1][j]


print(knapsack([10, 15, 40], [1, 2, 3], 6))

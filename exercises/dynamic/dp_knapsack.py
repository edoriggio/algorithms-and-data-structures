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

# Problem:
# Given weights and values of n items, put these items in a knapsack of
# capacity max_weight to get the maximum total value in the knapsack.

# Complexity:
# O(n*m)

def dp_knapsack(array, max_weight):
    memo = [[0 for _ in range(max_weight + 1)] for _ in range(len(array) + 1)]

    for i in range(len(memo)):
        for j in range(len(memo[0])):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif array[i-1][0] > j:
                    memo[i][j] = memo[i-1][j]
            else:
                if memo[i-1][j] > memo[i-1][j-array[i-1][0]] + array[i-1][1]:
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j-array[i-1][0]] + array[i-1][1]

    return memo[len(array)][max_weight]

print(dp_knapsack([(10, 50), (5, 40), (7, 30), (2, 10)], 9))

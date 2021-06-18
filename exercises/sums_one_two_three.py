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

# Time Complexity: O(n)
# Spacial Complexity: O(n)

def sum_one_two_three(n):
    dp = [0] * (n)

    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    # Complexity: O(n)
    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n-1]


# Time Complexity: O(n)
# Space Complexity: O(1)

def constant_space_one_two_three(n):
    one = 1
    two = 2
    three = 4

    for _ in range(3, n):
        tmp = one + two + three

        one = two
        two = three
        three = tmp

    return three


print(constant_space_one_two_three(4))

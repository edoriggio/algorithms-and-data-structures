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
# Find the n-th number of the Fibonacci sequence by only using dynamic
# programming and memoization.

# Complexity:
# O(n)

def dp_fib(n):
    memo = []

    for k in range(n):
        if k < 2:
            memo.append(1)
        else:
            next_n = memo[k-1] + memo[k-2]
            memo.append(next_n)

    return memo

print(dp_fib(10))
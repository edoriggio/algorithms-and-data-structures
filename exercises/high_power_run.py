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

def high_power_run(A, h, t):
    for i in range(len(A) - 1):
        curr_gain = 0
        max_sec = i + t

        if i + (t + 1) >= len(A):
            max_sec = len(A) - 1

        for j in range(i + 1, max_sec + 1):
            if A[j] > A[j - 1]:
                diff = A[j] - A[j - 1]
                curr_gain += diff

        if curr_gain >= h:
            return True

    return False


def high_power_run_n(A, h, t):
    start = 0
    gain = 0
    max_gain = 0

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            gain += A[i] - A[i - 1]

        if i >= t + 1:
            start += 1

        if start >= 1 and A[start] > A[start - 1]:
            gain -= A[start] - A[start - 1]

        if gain > max_gain:
            max_gain = gain

    if max_gain >= h:
        return True

    return False


arr = [10, 6, 1, 3, 2, 1, 3, 4, 6, 5, 6, 4, 3, 4]
print(high_power_run(arr, 6, 5))
print(high_power_run_n(arr, 6, 4))

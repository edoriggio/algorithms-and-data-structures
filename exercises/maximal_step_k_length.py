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

def maixmal_step_k_length(A, k):
    increasing = True
    curr_count = 1

    max_count = 1

    for i in range(len(A)-1):
        if (A[i] + k == A[i + 1]):
            if not increasing:
                if curr_count > max_count:
                    max_count = curr_count

                increasing = True
                curr_count = 1

            curr_count += 1
        elif (A[i] - k == A[i + 1]):
            if increasing:
                if curr_count > max_count:
                    max_count = curr_count

                increasing = False
                curr_count = 1

            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count

            curr_count = 1

    if curr_count > max_count:
        max_count = curr_count

    return max_count


arr = [2, 4, 5, 6, 8, 6, 4, 2, 0, 2, 4, 6, 10, 3, 1]
print(maixmal_step_k_length(arr, 2))

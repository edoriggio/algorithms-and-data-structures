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

# Complexity: O(n^2 * m)

def longest_common_prefix(A):
    max_len = 0

    for i in range(len(A)-1):
        smallest_str = ""
        largest_str = ""

        for j in range(i+1, len(A)):
            count = 0

            if len(A[i]) < len(A[j]):
                smallest_str = A[i]
                largest_str = A[j]
            else:
                smallest_str = A[j]
                largest_str = A[i]
            
            for k in range(len(smallest_str)):
                if smallest_str[k] == largest_str[k]:
                    count += 1

                    if k == len(smallest_str) - 1:
                        if count > max_len:
                            max_len = count
                else:
                    if count > max_len:
                        max_len = count

                    break

    return max_len


arr = ["ciao", "lugano", "bella"]
print(longest_common_prefix(arr))

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

# Compexity: O(n^2)

def most_congested_segment(A, l):
    s = e = 0
    max_count = 0

    for i in range(len(A)-1):
        count = 0
        max_end = A[i] + l

        for j in range(i+1, len(A)):
            if A[j] > max_end:
                if count > max_count:
                    s = A[i]
                    e = A[j-1]
                    max_count = count

                break
            
            count += 1

    return (s, e)


arr = [2, 5, 7, 9, 11, 15, 20, 28, 40]
print(most_congested_segment(arr, 5))            

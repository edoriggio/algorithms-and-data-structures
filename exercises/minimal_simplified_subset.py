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

# Complexity: O(n^3)

from math import inf

def minimal_simplified_subset(A):
    tmp = []

    for i in range(len(A) - 2):
        if A[i] == inf:
                continue

        for j in range(i+1, len(A) - 1):
            if A[j] == inf:
                continue

            for k in range(i+1, len(A)):
                if j == k or A[k] == inf:
                    continue

                if A[i] + A[j] == A[k]:
                    A[i] = inf
                    A[j] = inf
                    A[k] = inf

    for i in range(len(A)):
        if A[i] != inf:
            tmp.append(A[i])

    return tmp


arr = [7, 89, 11, 88, 106, 4, 28, 71, 17, 15]
print(minimal_simplified_subset(arr))

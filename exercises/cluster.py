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

# Compolexity: O(n^2)

def cluster(A):
    i = 0

    # Complexity: O(n)
    while i < len(A)-1:
        current = i

        # Complexity: O(n)
        for j in range(i+1, len(A)):
            if equals(A[j], A[i]):
                A[j], A[i+1] = A[i+1], A[j]
                i += 1
        
        if i == current:
            i += 1

    return A


def equals(x, y):
    return x == y


array = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
print(cluster(array))

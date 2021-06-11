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

# Return True if there are two identical subsequences in both A and B of
# minimum length k.

def algo_x(A, B, k):
    # Complexity: O(n)
    for i in range(len(A)-k+1):
        d = 0
        j = 0

        # Complexity: O(n)
        while j+k-1 < len(B):
            if d == k:
                return True
            elif A[i+d] == B[j+d]:
                d += 1
            else:
                d = 0
                j += 1

    return False


def better_algo_y(A, B):
    A.sort()
    B.sort()

    for i in range(min(len(A), len(B))):
        if A[i] == B[i]:
            return False

    return True


array_a = [1, 2, 3, 4, 5, 5]
array_b = [6, 7, 8, 9, 10]
print(better_algo_y(array_a, array_b))

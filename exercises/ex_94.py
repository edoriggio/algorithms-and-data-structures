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

# Complexity : O(n^3)

def equals(p, q):
    if p[0] == q[0] and p[1] == q[1]:
        return True

    return False


def algo_x(A):
    # Complexity: O(n)
    for i in range(len(A)):
        # Complexity: O(n)
        for j in range(len(A)):
            if equals(A[i][1], A[j][0]):
                # Complexity: O(n)
                for k in range(len(A)):
                    if equals(A[j][1], A[k][1]) and equals(A[i][0], A[k][0]):
                        return True

    return False

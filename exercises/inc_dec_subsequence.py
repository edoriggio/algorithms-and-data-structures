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

def inc_dec_subsequence(A, k, certificate):
    j = 0

    # Complexity: O(n)
    if len(certificate) < k or not is_sorted(certificate):
        return False

    # Complexity O(n)
    for i in range(len(A)):
        if j < len(certificate) and A[i] == certificate[j]:
            j += 1

    if j == len(certificate):
        
        return True

    return False


def is_sorted(A):
    increasing = True

    if len(A) > 1 and A[0] < A[1]:
        increasing = False

    for i in range(len(A)-1):
        if increasing and A[i] < A[i+1]:
            return False
        elif not increasing and A[i] > A[i+1]:
            return False

    return True


array = [2, 5, 9, 8, 1, 2, 4, 1, 0, -1, 10]
cert = [2, 1, 0, -1]
print(inc_dec_subsequence(array, 4, cert))

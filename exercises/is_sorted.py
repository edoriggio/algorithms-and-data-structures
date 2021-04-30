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

def is_sorted(A):
    increasing = True

    if len(A) > 1 and A[0] < A[1]:
        increasing = False

    # For loop -> n
    for i in range(len(A)-1):
        if increasing and A[i] < A[i+1]:
            return False
        elif not increasing and A[i] > A[i+1]:
            return False

    return True


arr = [1, 2, 3, 2, 3, 7, 8, 9]
arr1 = [9, 8, 7, 6, 4, 3, 2, 1, 1]
print(is_sorted(arr))
print(is_sorted(arr1))

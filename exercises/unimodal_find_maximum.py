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

# Complexity: O(log(n))

def unimodal_find_maximum(A):
    low = 0
    high = len(A) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
            high = mid - 1
        elif A[mid + 1] > A[mid] and A[mid] > A[mid - 1]:
            low = mid + 1
        else:
            return A[mid]


arr = [1, 5, 19, 17, 12, 8, 5, 3, 2]
print(unimodal_find_maximum(arr))

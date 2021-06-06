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

from math import ceil


def lower_bound(A, x):
    while len(A) > 0:
        mid = ceil(len(A) / 2) - 1

        if ((mid+1 < len(A)) and (A[mid+1] > x and A[mid] < x)):
            return A[mid+1]
        elif (A[mid-1] < x and A[mid] > x):
            return A[mid]
        elif (A[mid] == x):
            return A[mid]

        if len(A) == 1 and A[mid] > x:
            return A[mid]

        if x < A[mid]:
            A = A[:mid]
        elif x > A[mid]:
            A = A[mid+1:]
    else:
        return None


array = [2, 4, 5, 7, 8, 11, 15, 16, 20]
print(lower_bound(array, 12))

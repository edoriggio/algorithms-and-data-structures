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

def upper_bound(A, x):
    upper_bound = None

    # For loop -> n
    for i in range(len(A)):
        if A[i] == x:
            return A[i]
        elif A[i] > x and upper_bound == None:
            upper_bound = A[i]
        elif A[i] > x and A[i] < upper_bound:
            upper_bound = A[i]

    return upper_bound


def sorted_upper_bound(A, x):
    low = 0
    high = len(A) - 1

    if A[high] < x:
        return None
    elif A[high] >= x:
        return A[low]

    # While loop -> log(n)
    while low <= high:
        mid = (high + low) // 2

        if A[mid] < x:
            low = mid
        elif A[mid] == x:
            return A[mid]
        else:
            high = mid

    return A[high]


arr = [2, 5, 9, 20, 1, 2, 7, 9, 10, 15]
arr1 = [1, 2, 3, 4, 6, 7, 8, 9, 14, 15, 20, 25]
print(upper_bound(arr, 3))
print(sorted_upper_bound(arr1, 3))

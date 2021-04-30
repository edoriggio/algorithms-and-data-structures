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

def sum_of_three(A, s):
    # Merge sort -> nlog(n)
    A = merge_sort(A, 0, len(A))

    # 1st for loop -> n
    for i in range(len(A)-2):
        k = len(A) - 1
        j = i + 1

        # 2nd for loop (nested) -> n
        while k != j:
            if A[i] + A[j] + A[k] > s:
                k -= 1
            elif A[i] + A[j] + A[k] < s:
                j += 1
            else:
                return True

    return False


def merge_sort(A, begin, end):
    if end - begin == 1:
        return [A[begin]]
    elif end - begin == 0:
        return []

    m = (begin + end) // 2
    L = merge_sort(A, begin, m)
    R = merge_sort(A, m, end)

    return merge(L, R)


def merge(numbs1, numbs2):
    sorted_numbs = []
    i = j = 0

    while i < len(numbs1) and j < len(numbs2):
        if numbs1[i] <= numbs2[j]:
            sorted_numbs.append(numbs1[i])
            i += 1
        elif numbs2[j] <= numbs1[i]:
            sorted_numbs.append(numbs2[j])
            j += 1
        else:
            sorted_numbs.append(numbs1[i])
            i += 1
            j += 1

    if i < len(numbs1):
        for k in range(i, len(numbs1)):
            sorted_numbs.append(numbs1[k])

    if j < len(numbs2):
        for l in range(j, len(numbs2)):
            sorted_numbs.append(numbs2[l])

    return sorted_numbs


arr = [15, 2, 3, 1, 4, 5, 2, 1, 48, 51, 22]
print(sum_of_three(arr, 10))

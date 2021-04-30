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

# Complexity: O(nlog(n))

def peak_order(A):
    mid = len(A) // 2 - 1

    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        
        return A
    elif len(A) == 1:
        return A

    A = merge_sort(A, 0, len(A)-1)
    A = reverse(A, mid, len(A)-1)

    return A


def reverse(A, b, e):
    i = b
    j = e

    while i != j:
        A[i], A[j] = A[j], A[i]

        if (i + 1 == j):
            break

        i += 1
        j -= 1

    return A


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


arr = [2, 6]
print(peak_order(arr))

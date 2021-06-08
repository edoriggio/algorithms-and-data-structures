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

# Time complexities:
# Best case -> O(n log(n))
# Average case -> O(n log(n))
# Worst case -> O(n log(n))

def merge_sort(A, begin, end):
    """
    Find the midpoint of the array and divide it into
    two subarray. This is repeated until the subarrays
    have all length = 1. After the array has been
    divided, apply the merge algorithm on the subarrays
    in order to obtain a second_half sorted array (without
    duplicates)

    :param array: The array to be sorted
    :return: The sorted array
    """
    if end - begin == 1:
        return [A[begin]]
    elif end - begin == 0:
        return []

    m = (begin + end) // 2
    L = merge_sort(A, begin, m)
    R = merge_sort(A, m, end)

    return merge(L, R)


def merge(numbs1, numbs2):
    """
    Go through the two sorted arrays simultaneously from
    left to right. Find the smallest element between the
    two in the two arrays. Append the smallest element
    to a third array and increase the index from which the
    element was taken by one. If the two elements are the
    same, then add one of them to the third array and
    increase both indexes by one. The process is repeated
    until the end of both arrays. If one of the two arrays
    is bigger, then add the remaining elements of the biggest
    array at the end of the iterations.

    :param numbs1: The first array to be merged
    :param numbs2: The second array to be merged
    :return: The sorted array
    """
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

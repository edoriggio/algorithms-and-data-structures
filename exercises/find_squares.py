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

def find_squares(P):
    P = merge_sort(P, 0, len(P))

    for i in range(len(P)-1):
        found_i_y = binary_search(P, P[i][1], 1)

        for j in range(i+1, len(P)):
            found_j_y = binary_search(P, P[j][1], 1)

            if P[i][0] == P[j][0] and found_i_y and found_j_y:
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


def merge(A, B):
    i = j = 0
    sorted_arr = []

    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or A[i] <= B[j]):
            sorted_arr.append(A[i])
            i = i + 1
        else:
            sorted_arr.append(B[j])
            j = j + 1

    return sorted_arr

def order_2d(p1, p2):
    if p1[0] < p2[0]:
        return True
    elif p1[0] > p2[0]:
        return False
    elif p1[1] < p2[1]:
        return True
    elif p1[1] < p2[1]:
        return False

def binary_search(A, x, y):
    low = 0
    high = len(A) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if A[mid][i] < x:
            low = mid + 1
        elif A[mid][i] > x:
            high = mid - 1
        else:
            return True

    return False


arr = [(1, 5), (9, 4), (4, 5), (4, 2), (7, 3), (1, 9), (1, 2)]
print(find_squares(arr))

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

def maximal_score(A, B):
    points = 0

    for i in range(len(A)-1):
        if i >= len(A) or i >= len(B):
            break

        check_1 = check_points(A[i], B[i])
        check_2 = check_points(A[i+1], B[i])
        check_3 = check_points(A[i], B[i+1])

        if check_2 > check_1 and check_2 > check_3:
            A = reverse(A, i, len(A)-1)
            del A[-1]
            A = reverse(A, i, len(A)-1)
            points += check_2
        elif check_3 > check_1 and check_3 > check_2:
            B = reverse(B, i, len(B)-1)
            del B[-1]
            B = reverse(B, i, len(B)-1)
            points += check_3
        else:
            points += check_1

    return points


def check_points(a, b):
    if a == b:
        return 3
    elif a == b**2 or b == a**2:
        return 9
    elif a != b and (b % a == 0 or a % b == 0):
        return 5
    else:
        return 1


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


array_A = [4, 9, 5, 100]
array_B = [1, 2, 2, 10, 3]
print(maximal_score(array_A, array_B))

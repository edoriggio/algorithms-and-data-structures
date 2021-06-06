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

def partition_zero(A):
    k = 0
    i = 1
    j = len(A) - 1

    # Complexity: O(n)
    if not in_order(A):
        while i < j:
            if A[i] < 0:
                A[i], A[k] = A[k], A[i]
                k += 1
            elif A[i] > 0:
                A[i], A[j] = A[j], A[i]
                j -= 1

            i += 1

    end_neg = -1
    end_pos = -1

    # Complexity: O(n)
    for i in range(len(A)):
        if i > 0 and (A[i] >= 0 and A[i-1] < 0):
            end_neg = i-1
        
        if A[i] > 0 and end_pos == -1:
            end_pos = i

        if A[i] < 0 and end_neg != -1:
            A[i], A[end_neg+1] = A[end_neg+1], A[i]
            end_neg += 1
        
        if A[i] == 0 and end_pos != -1:
            A[i], A[end_pos] = A[end_pos], A[i]
            
            if end_pos + 1 < len(A):
                end_pos += 1

    return A


def in_order(A):
    neg = -1
    zero = -1
    pos = -1

    # Complexity: O(n)
    for i in range(len(A) - 1):
        if A[i] < 0 and pos == -1 and zero == -1:
            neg += 1
        elif A[i] < 0 and pos != -1 and zero != -1:
            return False
        elif A[i] == 0 and pos == -1:
            zero += 1
        elif A[i] == 0 and pos != -1:
            return False
        elif A[i] > 0 and neg != -1 and zero != -1:
            return False
        elif A[i] > 0:
            pos += 1

    if neg < zero < pos:
        return True
    else:
        return False


print(partition_zero([2, 5, 0, -1, 3, -7, 0, 3, -1, 10]))
print(partition_zero([-4, -3, -9, -7, 3, 2, 0, 0, 5, 9]))

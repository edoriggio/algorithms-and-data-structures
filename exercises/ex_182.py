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

# Complexity: O(2^n)

# This algorithm checks if s can be obtained by adding a subset
# of the elements of A together in a set A with n elements there
# are 2^n subsets. The worst case is where the number is never
# found, which means that the entire set of subsets has to be
# checked. The best case is the one in which the len(A) == 0 or
# s == 0 in both cases the answer is found immediately.

def sum_a(A, s):
    return sum_r(A, s, 0, len(A)-1)


def sum_r(A, s, b, e):
    if b > e and s == 0:
        return True
    elif b <= e and sum_r(A, s, b + 1, e):
        return True
    elif b <= e and sum_r(A, s-A[b], b+1, e):
        return True
    else:
        return False


arr = [1, 1, 1, 1, 1, 5, 4, 8, 6, 3, 10, 4, 8]
print(sum_a(arr, 0))

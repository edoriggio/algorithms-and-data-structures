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

# Complexity: O(n^3)

from math import inf

def longest_stretch(P, h):
    s = e = 0
    max_count = 0

    # 1st for loop -> n
    for i in range(len(P)-1):
        # 2nd for loop (nested) -> n
        for j in range(i+1, len(P)):
            count = is_sequence(P, i, j, h)

            if count > max_count:
                s = P[i][0]
                e = P[j-1][0]
                max_count = count

    return (s, e)


def is_sequence(P, b, e, h):
    max_h = -inf
    min_h = +inf
    count = 0

    # 3rd for loop (nested) -> n
    for i in range(b, e+1):
        if P[i][1] > max_h:
            max_h = P[i][1]

        if P[i][1] < min_h:
            min_h = P[i][1]

        count += 1

    if max_h - min_h > h:
        return -1
    
    return count


arr = [(1, 9), (3, 8), (4, 6), (9, 1)]
print(longest_stretch(arr, 7))

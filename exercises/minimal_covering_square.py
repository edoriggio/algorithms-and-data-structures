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

from math import inf


def minimal_covering_square(P):
    max_y, max_x = -inf, -inf
    min_y, min_x = +inf, +inf

    for i in range(len(P)):
        if P[i][0] > max_x:
            max_x = P[i][0]

        if P[i][1] > max_y:
            max_y = P[i][1]

        if P[i][0] < min_x:
            min_x = P[i][0]

        if P[i][1] < min_y:
            min_y = P[i][1]

    side_x = max_x - min_x
    side_y = max_y - min_y

    side_longest = side_x

    if side_y > side_longest:
        side_longest = side_y

    return side_longest * side_longest


points = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(minimal_covering_square(points))

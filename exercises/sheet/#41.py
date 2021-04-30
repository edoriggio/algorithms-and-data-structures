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

# Problem:
# Write an algorithm that takes a set of (x, y) coordinates representing
# points on a plane, and outputs the coordinates of two points with the
# maximal distance. The signature of the algorithm is Maximal-Distance(X,Y),
# where X and Y are two arrays of the same length representing the x and y
# coordinates of each point, respectively. Also, write the asymptotic
# complexity of Maximal-Distance. Briefly justify your answer.

# Complexity:
# O(n^2)

from math import inf, sqrt

def maximal_distance(xs, ys):
    max_distance = -inf
    max_distance_points = [-inf, -inf]

    for i in range(len(xs)-1):
        for j in range(1, len(xs)):
            distance = 0

            if xs[i] == xs[j]:
                distance = abs(ys[i] - ys[j])
            elif ys[i] == ys[j]:
                distance = abs(xs[i] - xs[j])
            else:
                distance_y = abs(ys[i] - ys[j])
                distance_x = abs(xs[i] - xs[j])
                distance = sqrt((distance_y ** 2) + (distance_x ** 2))
                
            if distance > max_distance:
                max_distance = distance
                max_distance_points[0] = (xs[i], ys[i])
                max_distance_points[1] = (xs[j], ys[j])

    return max_distance_points

print(maximal_distance([1,3,1,4], [1,2,4,5]))

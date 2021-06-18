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

# Given an array of points, find if there are at least 3 points that
# joined together form a right angle.

def algo_x(P):
    # Complexity: O(n)
    for i in range(len(P)):
        # Complexity: O(n)
        for j in range(len(P)):
            if j != i:
                ax = P[j][0] - P[i][0]
                ay = P[j][1] - P[i][1]

                # Complexity: O(n)
                for k in range(j+1, len(P)):
                    if k != i:
                        bx = P[k][0] - P[i][0]
                        by = P[k][1] - P[i][1]

                        if (ax * bx) + (ay + by) == 0:
                            return True

    return False


# Complexity: O(n^2)

def better_algo_x(P):
    x = [0] * (len(P)+1)
    DP = []

    # Complexity: O(n)
    for _ in range(len(P)+1):
        DP.append(x[:])

    # Complexity: O(n)
    for i in range(1, len(P)+1):
        # Complexity: O(n)
        for j in range(1, len(x)):
            if i == j:
                continue

            if DP[i-1][j] == 1:
                ax = P[j-1][0] - P[i-2][0]
                ay = P[j-1][1] - P[i-2][1]
                bx = P[i-1][0] - P[i-2][0]
                by = P[i-1][1] - P[i-2][1]

                if (ax * bx) + (ay * by) == 0:
                    return True
            else:
                if P[i-1][0] == P[j-1][0] \
                        or P[i-1][1] == P[j-1][1]:

                    DP[i][j] = 1

    return False


array = [(1, 5), (1, 2), (6, 2)]
print(better_algo_x(array))

# Copyright 2020 Edoardo Riggio
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
# Your sport watch is equipped with an altitude sensor that, every second,
# measures your altitude in meters. Given an array A = [a1, a2, ... , an]
# of n consecutive altitude measurements, you want to determine whether you
# had a high-power run. A high-power run occurs when there is a certain total
# altitude gain over a period of time, where the total altitude gain is the
# sum of all altitude gains (positive altitude variations) over that period.
# For example, the sequence of measurements 10, 10, 12, 11, 10, 11, 12
# corresponds to a total altitude gain of 4 meters.

# Complexity:
# O(n)

def high_power_run(array, min_distance, max_time):
    total_gain_seconds = []
    total = [0,0]
    seconds = 0
    gain = 0

    for i in range(len(array)-1):
        if array[i+1] > array[i]:
            gain += array[i+1] - array[i]
            seconds += 1
        elif array[i+1] <= array[i] and seconds > 0:
            total_gain_seconds.append((seconds, gain))
            seconds = gain = 0

    total = dp_helper(total_gain_seconds, max_time)

    if total >= min_distance:
        return True

    return False

def dp_helper(array, max_time):
    memo = [[0 for _ in range(max_time + 1)] for _ in range(len(array) + 1)]

    for i in range(len(memo)):
        for j in range(len(memo[0])):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif array[i-1][0] > j:
                    memo[i][j] = memo[i-1][j]
            else:
                if memo[i-1][j] > memo[i-1][j-array[i-1][0]] + array[i-1][1]:
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j-array[i-1][0]] + array[i-1][1]

    return memo[len(array)][max_time]

print(high_power_run([10,6,1,3,2,1,3,4,6,5,6,4,3,4], 6, 5))

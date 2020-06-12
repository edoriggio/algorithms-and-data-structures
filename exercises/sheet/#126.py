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
# The weather service stores the daily temperature measurements for each 
# city as vectors of real numbers.
# - Question 1: Write an algorithm called Hot-Days(A, t) that takes an array
#   A of daily temperature measurements for a city and a temperature t, and
#   returns the maximum number of consecutive days with a recorded temperature
#   above t. Also, analyze the complexity of Hot-Days(A, t).
# 
# - Question 2: Now imagine that a particular analysis would call the Hot-Days
#   algorithm several times with the same series A of temperature measurements
#   (but with different temperature values) and therefore it would be more
#   efficient to somehow index or precompute the results. To do that, write the
#   following two algorithms:
# 
#   • A preprocessing algorithm called Hot-Days-Init(A) that takes the series
#     of temperature measurements A and creates an auxiliary data structure X
#     (an index of some sort).
#   • An algorithm called Hot-Days-Fast(X, t) that takes the index X and a
#     temperature t and returns the maximum number of consecutive days with a
#     temperature above t. Hot-Days-Fast must run in sub-linear time in the 
#     size of A.

# Complexity:
# (1)(2) - O(n)
# (3) - O(1)

# (1)
def hot_days(array, temperature):
    max_consecutive = 0
    consecutive = 0

    for i in range(len(array)):
        if array[i] >= temperature:
            consecutive += 1
        else:
            max_consecutive = max(consecutive, max_consecutive)
            consecutive = 0

    return max(consecutive, max_consecutive)

# (2)
def hot_days_init(array):
    for temp in range(10):
        memo[temp] = hot_days(array, temp)

# (3)
def hot_days_fast(memo, temperature):
    return memo[temperature]

memo = {}
array_temps = [5,4,2,1,6,5,8,7,2,5,6,7,8,9,4,7]

hot_days_init(array_temps)
print(hot_days_fast(memo, 3))

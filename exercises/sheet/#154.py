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
# A system collects the positions of cars along a highway that connects
# two cities, A and B. The positions are grouped by direction in two arrays,
# A and B. Thus A contains the distances in kilometers from city A of the
# cars traveling towards city A. Write an algorithm Congestion(A) that takes
# the array A and prints a list of congested sections of the highway. A
# congested interval is a contiguous stretch of highway of 1km or more in
# which the density of cars is more than 50 cars per kilometer. Congestion(A)
# must run in O(nlogn) time.

# Complexity:
# O(nlogn)

def congestion(array):
    array.sort()
    congested = []
    counter = 0

    for i in range(len(array)-1):
        if array[i+1] != array[i] and counter >= 4:
            congested.append(array[i])
            counter = 0
        elif array[i+1] != array[i] and counter < 4:
            counter = 0
        elif array[i+1] == array[i]:
            counter += 1
        
        if i + 1 == len(array) - 1 and counter >= 4:
            congested.append(array[i])

    return congested

print(congestion([20,10,20,20,10,30,20,20,10,10,30,30,10,30,30,30,40]))

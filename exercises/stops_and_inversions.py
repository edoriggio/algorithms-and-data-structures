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

def stops_and_inversions(A):
    prev = -1
    last_stop = -1
    direction = 1

    stops = 0
    inversions = 0

    for i in A:
        if i == prev and last_stop != i:
            stops += 1
            last_stop = i
        elif i > prev:
            last_stop = -1
            
            if direction == -1:
                inversions += 1
                direction = 1
        elif i < prev:
            last_stop = -1

            if direction == 1:
                inversions += 1
                direction = -1
        
        prev = i

    print("Stops: {0}\nInversions: {1}".format(stops, inversions))


arr = [1,5,10,12,12,11,8,7,9,11,20,30,30,30,30,35,35]
stops_and_inversions(arr)

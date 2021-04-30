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
# Given a number k, a step-k sequence of length l is a sequence of l numbers
# a1, a2 , . . . , al such that either ai = ai+1 + k for all pairs of adjacent
# elements ai , ai+1, r ai + k = ai+1 for all pairs of adjacent elements ai,ai+1.
# For example, the sequence , 3.5, 5, 6.5, 8 is a step-1.5 sequence, and 7, 4, 1,
# −2 is a step-3 sequence.

#Complexity:
# O(n)

def maximal_step_k_length(array, step):
    max_counter = 0
    counter = 0
    increasing = False
    change = False

    for i in range(len(array)-1):
        if counter == 0 or change:
            change = False

            if array[i+1] == array[i] + step:
                increasing = True
                counter += 1
            elif array[i+1] == array[i] - step:
                increasing = False
                counter += 1
        elif increasing and array[i+1] == array[i] + step:
            counter += 1
        elif not increasing and array[i+1] == array[i] - step:
            counter += 1
        elif (array[i+1] != array[i] + step and increasing)\
              or (array[i+1] != array[i] + step and not increasing):
            max_counter = max(counter+1, max_counter)
            counter = 0

        if not increasing and array[i+1] == array[i] + step:
            max_counter = max(counter+1, max_counter)
            increasing = True
            change = True
            counter = 1
        elif increasing and array[i+1] == array[i] - step:
            max_counter = max(counter+1, max_counter)
            increasing = False
            change = True
            counter = 1

    return max_counter

print(maximal_step_k_length([2,4,5,6,8,6,4,2,0,2,4,6,10,3,1], 2))

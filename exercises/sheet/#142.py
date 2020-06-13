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

# Consider the following sorting problem: you must reorder the elements of an
# array of numbers in-place so that odd numbers are in odd positions while
# even numbers are in even positions. If there are more even elements than
# odd ones in A (or vice-versa) then those additional elements will be grouped
# at the end of the array.

# Complexity:
# O(n) -?

def alternate_even_odd(array):
    i = 0
    j = 1
    
    while i < len(array):
        if j < len(array):
            if i % 2 == 0:
                if array[i] % 2 == 0:
                    i += 1
                    j += 1
                elif array[j] % 2 == 0:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j = i + 1
                else:
                    j += 1
            else:
                if array[i] % 2 != 0:
                    i += 1
                    j += 1
                elif array[j] % 2 != 0:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j = i + 1
                else:
                    j += 1
        
        return array
    
print(alternate_even_odd([50,47,92,78,76,7,60,36,59,30,50,43]))

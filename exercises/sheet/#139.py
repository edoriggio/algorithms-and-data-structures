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
# Write an algorithm Print-In-Three-Columns(A) that takes an array of words
# A and prints all the words in A, in the given order left-to-right and
# top-to-bottom, such that the words are left-aligned in three columns.
# Words must be separated by at least one space horizontally, but in order
# to align words, the algorithm might have to print more spaces between words.

# Complexity:
# O(n)

def print_in_three_columns(array):
    max_in_cols = [0, 0, 0]
    counter = 0

    for i in range(len(array)):
        if counter == 0:
            if len(array[i]) > max_in_cols[0]:
                max_in_cols[0] = len(array[i])
            counter += 1
        elif counter == 1:
            if len(array[i]) > max_in_cols[1]:
                max_in_cols[1] = len(array[i])
            counter += 1
        else:
            if len(array[i]) > max_in_cols[2]:
                max_in_cols[2] = len(array[i])
            counter = 0

    counter = 0

    for i in array:
        if counter == 0:
            print(i + ' '*(max_in_cols[0] - len(i)), end=' ')
            counter += 1
        elif counter == 1:
            print(i + ' '*(max_in_cols[1] - len(i)), end=' ')
            counter += 1
        else:
            print(i + ' '*(max_in_cols[2] - len(i)))
            counter = 0

print_in_three_columns(['exam', 'algorithms', 'asymptotic', 'complexity',\
    'graph', 'greedy', 'lugano', 'np', 'quicksort', 'retake', 'september'])

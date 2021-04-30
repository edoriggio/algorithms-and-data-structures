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
# You are in front of a stack of pancakes of different diameter. Unfortunately,
# you cannot eat them unless they are sorted according to their size, with the
# biggest one at the bottom. To sort them, you are given a spatula that you can
# use to split the stack in two parts and then flip the top part of the stack.
# Write the an algorithm Sort-Pancakes(P) that sorts the stack P using only
# spatula-flip operations. The array P stores the pancakes top-to-bottom, thus
# P[0] is the size of the pancake at the top of the stack, while P [P.length]
# is the size of the pancake at the bottom of the stack. Your algorithm must
# indicate a spatula flip with the spatula inserted at position i with
# Spatula-Flip(P,i), which flips all the elements in P [0...i].

# Complexity:
# O(n^2)

def sort_pancake(array):
    temp = array
    res = []

    for _ in range(len(array)):
        maximum = index_of_max(temp)
        res.append(temp[maximum])
        spatula_flip(temp, maximum)
        temp = temp[1:]

    spatula_flip(res, len(res)-1)
    return res

def index_of_max(array):
    maximum = [0,0]

    for i in range(len(array)):
        if array[i] > maximum[1]:
            maximum[0] = i
            maximum[1] = array[i]

    return maximum[0]

def spatula_flip(array, maximum):
    for i in range(maximum):
        if i <= maximum//2:
            array[i], array[maximum-i] = array[maximum-i], array[i]

print(sort_pancake([2,4,1,5,9,7]))

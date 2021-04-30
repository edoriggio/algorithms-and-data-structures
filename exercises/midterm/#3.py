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
# An array A = [a1 , a2 , ... , an] of numbers is said to be in “peak”
# order ifai ≥ ai−1 for all 1 < i ≤ (n + 1)/2, and aj ≥ aj+1 for all
# (n + 1)/2 ≤ j < n. In essence, A is in peak order when its first half
# is in ascending order while the second half is in descending order. In
# a source file ex3.py, write a Python function called peak_order(A) that
# takes an array of numbers A and reorders its elements into a peak order.
# peak_order(A) must change the array A in-place, and must run in O(n log n)
# time.

# Complexity:
# O(nlogn)

def peak_order(array):
    j = 0
    mid = len(array) // 2
    array.sort()

    for i in range(mid, len(array)):
        if j < (len(array)-mid) // 2:
            array[i], array[len(array)-1-j] = array[len(array)-1-j], array[i]
            j += 1

    return array

print(peak_order([5,7,2,0,4,20,1,8,40]))

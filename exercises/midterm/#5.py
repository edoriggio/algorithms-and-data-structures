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
# Write a function is_sorted(A) that returns True if A issorted in either
# ascending or descending order. Analyze the complexity of is_sorted(A).

# Complexity:
# O(n)

def is_sorted(array):
    descending = False

    for i in range(len(array)-1):
        if array[i] > array[i - 1]:
            descending = True

    if not descending or sorted(array) == array:
        return True
    else:
        return False

print(is_sorted([1,5,6,7,9,20]))

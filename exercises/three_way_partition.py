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

def three_way_partition(A, begin, end):
    numb = 0
    pivot = 0

    for i in range(begin, end):

        if A[i] > numb:
            pivot = i
            numb = A[i]

    A[pivot], A[end-1] = A[end-1], A[pivot]

    i = begin
    j = end-2
    
    while i < j:
        if A[i] == numb:
            A[i], A[j] = A[j], A[i]
            j -= 1

        i += 1

    print(A)


arr = [100,2,100,200,200,10,0,98,2]
three_way_partition(arr, 0, len(arr))

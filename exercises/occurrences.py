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

# Complexity: O(n log(n))

def occurrences(A):
    counter = 1
    # Complexity: O(n log(n))
    A.sort()

    # Complexity: O(n)
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            print (f"{A[i-1]} {counter}")
            counter = 1
        else:
            counter += 1

    print(f"{A[-1]} {counter}")

array = [28, 1, 0, 1, 0, 3, 4, 0, 0, 3]
occurrences(array)

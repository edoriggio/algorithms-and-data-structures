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

# Complexity: O(n^2)

def find_elements_at_distance(A, k):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A) - 1):
            if A[j] - A[i] == k:
                return True
            elif A[j] - A[i] > k:
                continue

    return False


arr = [2, 5, 10, 15, 18, 20]
print(find_elements_at_distance(arr, 17))

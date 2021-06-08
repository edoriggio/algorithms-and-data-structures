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

def group_of_k(S, k):
    elems = []
    records = {}

    for i in range(len(S)):
        for j in range(len(S[i])):
            elems.append(((S[i][j]), i))

    for i in range(len(elems)):
        try:
            records[elems[i][0]] += 1
        except KeyError:
            records[elems[i][0]] = 1

    for key, value in records.items():
        if value == k:
            return key

    return None


array = [[(1, 1), (2, 2)], [(2, 5), (7, 2)], [(1, 3), (2, 2)]]
print(group_of_k(array, 2))

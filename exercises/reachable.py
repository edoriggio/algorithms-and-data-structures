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

def reachable_test(graph, k, certificate):
    if len(certificate) < k:
        return False

    for i in range(len(certificate)):
        for j in range(len(certificate)):
            found = False

            if certificate[j] == list(graph.keys())[list(graph.values()).index(graph[certificate[i]])]:
                continue

            for k in range(len(graph[certificate[i]])):
                if certificate[j] == graph[certificate[i]][k]:
                    found = True
                    break

            if not found:
                return False

    return True


graph = {1: [7, 4, 2, 6, 3], 2: [1, 3, 6, 5], 3: [1, 2, 6], 4: [1, 5],
         5: [2, 4], 6: [2, 1, 3], 7: [1]}
certificate = [1, 2, 3]
print(reachable_test(graph, 3, certificate))

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

# Complexity: O(n * m * m')
# Where n is the number of nodes, and m is the number of edges in graph_one.
# Where m' is the number of edges in graph_two.

def identical_graphs(graph_one, graph_two, certificate):
    # Complexity: O(n)
    for key, value in graph_one.items():
        # Complexity: O(m)
        for i in range(len(value)):
            found = False
            
            # Complexity: O(m')
            for j in range(len(graph_two[key])):
                if graph_two[key][j] == value[i]:
                    found = True

            if len(graph_two[key]) != len(value):
                found = False

            if not found and certificate:
                return False
            elif not found and not certificate:
                return True

    if not certificate:
        return False

    return True


graph_a = {1: [5, 2], 2: [1, 5], 3: [4], 4: [3, 5], 5: [1, 2, 4]}
graph_b = {2: [1, 5], 3: [4], 4: [3, 5], 5: [1, 2, 4], 1: [5, 2]}
print(identical_graphs(graph_a, graph_b, True))

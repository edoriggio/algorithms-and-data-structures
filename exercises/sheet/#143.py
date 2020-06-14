# Copyright 2020 Edoardo Riggio
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
# Write an algorithm called Four-Cycle(G) that takes a directed graph represented
# with its adjacency matrix G, and that returns true if and only if G contains a 4-cycle. A 4-cycle is a
# sequence of four distinct vertexes a, b, c, d such that there is an arc from a to b, from b to c, from
# c to d, and from d to a. Also, analyze the complexity of Four-Cycle(G).

# Complexity:
# O(|V|+|E|)

from graphs import *

def has_cycle(graph, vertex, stack, visited):
        visited.append(vertex)
        stack.append(vertex)
        for n in graph[vertex]:
            if n not in visited:
                if has_cycle(graph, n, visited, stack):
                    return True
            elif n in stack:
                return True
        stack.remove(vertex)
        return False

def four_cycle(graph):
    visited = []
    stack = []
    for v in graph:
        if v not in visited:
            if has_cycle(graph, v, stack, visited) and len(stack) == 4:
                return True
        visited = []
        stack = []
    return False

print(four_cycle(graph_letters_cycle_4))
print(four_cycle(graph_letters_cycle))
print(four_cycle(graph_no_cycles))

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

def dfs(graph):
    """Function that recreates the Breath First Search
    algorithm, using a stack as its data structure.
    In this algorithm, when a node is analyzed, it is
    marked as visited and the topologically smallest
    child is added to the stack (if their not in it 
    already). The next node to be analyzed is given 
    both by the stack and the 'visited' array. If a
    node is popped and it is not in the 'visited'
    array, then it is analyzed.

    Args:
        graph (dict): a dictionary mapping the graph of the graph
                      to their connections.

    Returns:
        array: the array of visited graph in order of visiting
    """

    visited = []

    for key in graph.keys():
        stack = [key]

        if key in visited:
            continue

        while stack:
            node = stack.pop()

            for i in range(len(graph[node])):
                stack.append(graph[node][i])

            if key not in visited:
                visited.append(node)
    
    return visited

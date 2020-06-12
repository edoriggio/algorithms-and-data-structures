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

# Time complexity -> Θ(|V|+|E|)

from graphs import *

def dfs_algo(graph, print_out = True):
    """
    Function that recreates the Breath First Search
    algorithm, using a stack as its data structure.
    In this algorithm, when a node is analyzed, it is
    marked as visited and the topologically smallest
    child is added to the stack (if their not in it 
    already). The next node to be analyzed is given 
    both by the stack and the 'visited' array. If a
    node is popped and it is not in the 'visited'
    array, then it is analyzed.

    Args:
        graph (dict): A dictionary representing the graph
                      to analyze
        print_out (Bool, default: True): Decide whether to
                                         print the steps

    Returns:
        (list): An array containing the nodes in the order
                of how they were visited
    """
    visited = []
    stack = [next(iter(graph))]

    while stack:
        element = stack.pop()

        for neighbor in reversed(graph[element]):
            if neighbor not in visited:
                if neighbor not in stack:
                    stack.append(neighbor)

        if element not in visited:
            visited.append(element)

        if print_out:
            print('Node:', element,\
                '  Stack:', stack,\
                '  Visited:', visited)

    return visited

print(dfs_algo(graph_numbers), end='\n\n')
print(dfs_algo(graph_letters, False), end='\n\n')

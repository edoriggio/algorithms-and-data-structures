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

# NOT WORKING

from graphs import graph_dijkstra
from math import inf

def dijkstra(graph, start):
    path = [start]
    neighbors = graph[start]
    preceding = +inf
    cost = []

    for node in graph:
        if node in neighbors:
            if neighbors[node] < cost:
                cost.append(neighbors[node])
                print(node)
                print(cost)
                print()

            preceding = node
        else:
            cost.append(+inf)

    while path != graph.keys():
        min_node = [+inf, +inf]

        for node in neighbors:
            if neighbors[node] not in path:
                if neighbors[node] < min_node[1]:
                    min_node[0] = node
                    min_node[1] = neighbors[node]

        path.append(min_node[0])

        for neighbor in graph[min_node[0]]:
            print(neighbor)
            print(min_node[1] + graph[min_node[0]][neighbor], cost)
            print(min_node[1] + graph[min_node[0]][neighbor] < cost)
            print()
            if neighbor not in path:
                if min_node[1] + graph[min_node[0]][neighbor] < cost:
                    cost = min_node[1] + graph[min_node[0]][neighbor]
                    preceding = min_node[0]

        print(neighbors)
        print(min_node)
        print(path)
        print()
        break


dijkstra(graph_dijkstra, 'a')

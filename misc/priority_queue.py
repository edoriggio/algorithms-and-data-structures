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

class Priority_Queue:
    """
    This class represents a priority queue. In this data
    structure elements are retrieved form the queue (i.e.
    dequeued) in descending order based on the priority
    of the element.
    """

    data: list

    def __init__(self):
        self.data = []

    def parent(self, element: int) -> int:
        """
        Find the index of the parent node of a given node.

        Args:
            element (int): The index of the node to be checked

        Returns:
            (int) The index of the parent node
        """
        return (element-1) // 2

    def left(self, element: int) -> int:
        """
        Find the index of the left child node of a given node.

        Args:
            element (int): The index of the node to be checked

        Returns:
            (int) The index of the left child node
        """
        return 2 * element + 1

    def right(self, element: int) -> int:
        """
        Find the index of the right child node of a given node.

        Args:
            element (int): The index of the node to be checked

        Returns:
            (int) The index of the right child node
        """
        return 2 * element + 2

    def enqueue(self, element: int, priority: int):
        """
        Add the new node containing the tuple (element, priority)
        to the priority queue.

        Args:
            element (int): The value of the node
            priority (int): The priority of the node
        """
        self.data.append((element, priority))
        i = len(self.data) - 1

        while i > 0 and self.data[i][1] > self.data[self.parent(i)][1]:
            tmp = self.data[i]
            self.data[i] = self.data[self.parent(i)]
            self.data[self.parent(i)] = tmp
            i = self.parent(i)

    def dequeue(self) -> None:
        """
        Remove the nodes in descending order based on their
        priority.

        Returns:
            (None): Nothing
        """
        if len(self.data) == 0:
            print('Priority Queue Underflow')
            return

        result = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]

        i = 0
        m = 0

        while True:
            if self.left(i) < self.left(m):
                if self.data[m][1] < self.data[self.left(i)][1]:
                    m = self.left(i)
                if self.right(i) < len(self.data) and self.data[m][1] < self.data[self.right(i)][1]:
                    m = self.right(i)
            if m != i:
                tmp = self.data[i]
                self.data[i] = self.data[m(i)]
                self.data[m] = tmp
                i = m
            else:
                break

        print(result)

    def print_self(self):
        """
        Print the data and the length values of the priority queue.
        """
        print('Data: {} Length: {}'.format(self.data, len(self.data)))

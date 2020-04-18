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

import sys

class Queue:
    """
    This class represents a queue. A queue is a FIFO data
    structure (First In First Out) of fixed size. When
    initialized, it creates a queue of a number of None
    objects equal to the length that is given as a parameter.

    Args:
        length (int): The length of the queue

    Attributes:
        length (int): The length of the queue
        top (int): The index of the last element of the queue
        data (list): The data contained in the queue
    """
    def __init__(self, length: int):
        self.length = length
        self.data = [None] * self.length
        self.head = 0
        self.tail = 0

    def queue_next(self, element: int) -> int:
        """
        Check which is the succeding index of the
        one given.

        Args:
            element (int): The element to check

        Returns:
            (int): The index of the succeding element
        """
        if element == self.length - 1:
            return 0
        else:
            return element + 1

    def enqueue(self, element: int) -> None:
        """
        Check if the queue is full. If it is not full, then
        add the element given at the bottom of the queue.

        Args:
            element (int): The element to add

        Returns:
            (None) Nothing
        """
        if self.check_full():
           print('Queue Overflow')
           return

        self.data[self.tail] = element
        self.tail = self.queue_next(self.tail)

    def dequeue(self) -> None:
        """
        Check if the queue is empty. If it is not empty, then
        remove the first element of the queue and prints it.

        Returns:
            (None) Nothing
        """
        if self.check_empty():
            print('Queue Underflow')
            return

        removed = self.data[self.head]
        self.data[self.head] = None
        self.head = self.queue_next(self.head)
        print(removed)

    def check_empty(self) -> bool:
        """
        Check if all the elements in the queue
        are None objects.

        Returns:
            (bool) True if the queue is empty
                   False if the queue is not empty
        """
        for i in self.data:
            if i != None:
                return False

        return True

    def check_full(self) -> bool:
        """
        Check if all the elements in the queue
        are not None objects.

        Returns:
            (bool) True if the queue is full
                   False if the queue is not full
        """
        for i in self.data:
            if i == None:
                return False

        return True

    def print_self(self):
        """
        Print the data, head and tail values of the queue.
        """
        print('Data: {}\nHead: {}, Tail: {}'.format(self.data, self.head, self.tail))

test_queue: Queue

# Driver
for l in sys.stdin:
    l = l.split()

    if len(l) == 0:
        print('%')
        continue

    if l[0] == 'init':
        test_queue = Queue(int(l[1]))
        print('%')

    if l[0] == '+':
        test_queue.enqueue(int(l[1]))
        print('%')

    elif l[0] == '-':
        test_queue.dequeue()
        print('%')

    elif l[0] == 'print':
        test_queue.print_self()
        print('%')

    else:
        print('unknown command:', l[0])
        print('%')

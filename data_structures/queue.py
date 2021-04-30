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

class Queue:
    """Class for the fixed-size Queue data structure. It contains the data and
    metadata of the Queue.
    """
    queue: list
    length: int

    tail: int
    head: int

    empty: bool
    full: bool

    def __init__(self, length):
        self.queue = [None] * length
        self.length = length
        self.head = self.tail = 0
        self.empty = True
        self.full = False

    def enqueue(self, value):
        """Insert the given value at the tail pointer of the Queue, return
        error if overflow occurs.

        Args:
            value (void): a value to be inserted into the Queue
        """
        if not self.full:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.length
            self.empty = False
        elif self.full:
            print("OVERFLOW")
            return

        self.full = self.tail == self.head

    def dequeue(self):
        """Remove the item to which 'head' is pointing from the Queue.

        Returns:
            void: the removed element
        """
        if not self.empty:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.length
            self.full = False
        elif self.empty:
            print("UNDERFLOW")
            return

        self.empty = self.head == self.tail
        return value

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

class LinkedList:
    """Class that contains the elements of a doubly linked list with a
    sentinel.
    """
    sentinel: None

    class LinkedListElement:
        """The single elements of the doubly linked list.
        """
        value: None
        prev: None
        nxt: None

        def __init__(self):
            self.value = None
            self.prev = None
            self.nxt = None

    def __init__(self):
        self.sentinel = self.LinkedListElement()

        self.sentinel.value = None
        self.sentinel.nxt = self.sentinel
        self.sentinel.prev = self.sentinel

    def insert_after(self, element, value):
        """Insert a new element with a given new value after the
        given element.

        Args:
            element (LinkedListElement): the element before the new
                                         element
            value (void): the value to insert
        """
        new_element = self.LinkedListElement()

        new_element.value = value
        new_element.prev = element
        new_element.nxt = element.nxt

        new_element.prev.nxt = new_element
        new_element.next.prev = new_element

    def insert_before(self, element, value):
        """Insert a new element with a given new value before the
        given element.

        Args:
            element (LinkedListElement): the element after the new
                                         element
            value (void): the value to insert
        """
        new_element = self.LinkedListElement()

        new_element.value = value
        new_element.prev = element.prev
        new_element.nxt = element

        new_element.prev.nxt = new_element
        new_element.next.prev = new_element

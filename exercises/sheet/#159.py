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
# We say that two words x and y are linked to each other if they differ by
# a single letter, or more specifically by one edit operation, meaning an
# insertion, a deletion, or a change in a single character. For example,
# “fun” and “pun” are linked, as are “flower” and “lower”, “port” and
# “post”, “canton” and “cannon”, and “cat” and “cast”. Write an algorithm
# Linked(x, y) that takes two words x and y and, in lienar time, returns
# true if x and y are linked to each other, or false otherwise.

# Complexity:
# O(n)

def linked(word_1, word_2):
    counter = 0

    if len(word_1) > len(word_2) or len(word_1) < len(word_2):
        return False
    else:
        for i in range(len(word_1)):
            if word_1[i] != word_2[i]:
                counter += 1

        if counter > 1:
            return False
        
    return True

    print(longest, shortest)

print(linked('list', 'last'))

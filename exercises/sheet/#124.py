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

# Problem:
# Consider a social network system that, for each user u, stores u’s friends
# in a list friends(u). Implement an algorithm Top-Three-Friends-Of-Friends(u)
# that, given a user u, recommends the three other users that are not already
# among u’s friends but are among the friends of most of u’s friends. Also,
# analyze the complexity of the Top-Three-Friends-Of-Friends algorithm.

# Complexity:
# O(n^2)

from graphs import user_network

def top_three_friends_of_friends(user):
    memo = {}
    top_three = []

    for i in user:
        for j in user[i]:
            if j not in memo:
                memo[j] = 1
            else:
                memo[j] += 1

    for _ in range(3):
        current_maximum = (0,0)

        for i in memo:
            if memo[i] > current_maximum[1]:
                current_maximum = (i, memo[i])
        
        top_three.append(current_maximum[0])
        memo[current_maximum[0]] = -1

    return top_three

print(top_three_friends_of_friends(user_network))

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

# Complexity: O(n^2)

def two_primes(number):
    # Complexity: O(n^2)
    primes = find_primes(number)

    if primes[-1] == number:
        del primes[-1]

    x = [0] * (number+1)
    DP = []

    # Complexity: O(n * len(primes))
    for _ in range(len(primes)+1):
        DP.append(x[:])

    for i in range(1, number+1):
        for j in range(1, len(x)):
            if i-1 >= len(primes):
                return DP[-1][-1] == number

            if j >= primes[i-1]:
                DP[i][j] = max(DP[i-1][j], primes[i-1] +
                               DP[i-1][j - primes[i-1]])
            else:
                DP[i][j] = DP[i-1][j]


# Complexity: O(n^2)
def find_primes(number):
    primes = []

    for i in range(2, number+1):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes


print(two_primes(11))

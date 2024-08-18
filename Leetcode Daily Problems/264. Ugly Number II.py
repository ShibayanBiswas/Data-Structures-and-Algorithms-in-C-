"""
01. Initialize Primes and Data Structures:
   - `primes`: A list of prime factors [2, 3, 5].
   - `uglyHeap`: A min-heap initialized with the first ugly number, 1.
   - `visited`: A set to keep track of numbers that have already been processed to avoid duplicates.

02. Generate Ugly Numbers:
   - For `n` iterations, pop the smallest element from `uglyHeap` (this is the current smallest ugly number).
   - For each prime in `primes`, multiply it with the current smallest ugly number to generate a new potential ugly number.
   - If this new ugly number hasn't been processed before (not in `visited`), push it onto `uglyHeap` and add it to `visited`.

03. Return the nth Ugly Number: After `n` iterations, the smallest element popped from `uglyHeap` is the nth ugly number.

Time Complexity: O(n log n), where n is the position of the ugly number. Each push and pop operation on the heap takes O(log n) time.
Space Complexity: O(n), due to the space required for the heap and the set `visited`.
"""

from heapq import heappop, heappush

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 01. Initialize the primes and data structures
        primes = [2, 3, 5]
        uglyHeap = [1]  # Min-heap initialized with the first ugly number
        visited = set()  # Set to keep track of seen ugly numbers
        visited.add(1)
        
        # 02. Generate ugly numbers
        for _ in range(n):
            curr = heappop(uglyHeap)  # Pop the smallest element from the heap
            
            # Generate new ugly numbers by multiplying with the primes
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)
        
        # 03. Return the nth ugly number
        return curr
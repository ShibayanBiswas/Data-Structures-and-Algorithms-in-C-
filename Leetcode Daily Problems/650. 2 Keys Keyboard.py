"""
01. Handle Base Case: If `n` is 1, return 0 because no operations are needed to get exactly one 'A' on the screen.

02. Initialize Variables: 
   - `steps`: To count the total number of operations.
   - `factor`: Start with 2, as it is the smallest factor to consider for dividing `n`.

03. Factorization Process: 
   - While `n` is greater than 1, find the smallest factor `factor` that divides `n`.
   - For each such factor, divide `n` by `factor` and add `factor` to `steps`. This represents performing `factor` operations (copy and paste).
   - Increment the factor and repeat until `n` becomes 1.

04. Return the Result: Once the factorization process is complete and `n` is reduced to 1, return the total `steps` required.

Time Complexity: O(sqrt(n)), since we only need to check up to the square root of `n` for factors.
Space Complexity: O(1), since the solution uses a constant amount of extra space.
"""

class Solution:
    def minSteps(self, n: int) -> int:
        # 01. Handle the base case where n is 1
        if n == 1:
            return 0
        
        # 02. Initialize variables
        steps = 0
        factor = 2
        
        # 03. Factorization process
        while n > 1:
            while n % factor == 0:  # Check if factor divides n
                steps += factor  # Add factor to the total steps
                n //= factor  # Reduce n by dividing it by the factor
            factor += 1  # Move to the next factor
        
        # 04. Return the total number of steps
        return steps
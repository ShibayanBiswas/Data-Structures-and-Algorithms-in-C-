"""
01. Initialize DP Table:
   - `n`: Length of the string `s`.
   - `dp`: A 2D list initialized with -1, where `dp[i][j]` will store the minimum number of turns required to print the substring from index `i` to `j`.

02. Define Recursive Utility Function:
   - Base Case: If `i` is greater than `j`, return 0 because an empty substring requires no turns.
   - If the value of `dp[i][j]` is already computed (not equal to -1), return the stored value to avoid recomputation.

03. Calculate the Minimum Turns:
   - Start by assuming that the first character at index `i` needs one turn, and recursively compute the turns required for the substring starting from `i + 1` to `j`.
   - Then, iterate over the substring from `i + 1` to `j`. If a character at position `k` matches the character at `i`, try splitting the problem into two subproblems:
     - One for the substring from `i` to `k - 1`.
     - The other for the substring from `k + 1` to `j`.
   - Update the `dp[i][j]` with the minimum turns required.

04. Return the Result:
   - The result is stored in `dp[0][n-1]`, representing the minimum number of turns required to print the entire string.

Time Complexity: O(n^3), where n is the length of the string `s`. The solution involves nested loops iterating over substrings.
Space Complexity: O(n^2), due to the 2D DP table storing the results of subproblems.
"""

class Solution:
    def strangePrinter(self, s: str) -> int:
        # 01. Initialize DP table
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        
        # 02. Call the recursive utility function to get the result
        return self.Util(0, n - 1, s, dp)

    def Util(self, i: int, j: int, s: str, dp: list) -> int:
        # Base case: If i > j, return 0
        if i > j:
            return 0

        # If already computed, return the stored result
        if dp[i][j] != -1:
            return dp[i][j]

        # 03. Calculate the minimum turns starting with the first character
        first_letter = s[i]
        answer = 1 + self.Util(i + 1, j, s, dp)

        # Check for matching characters in the substring and update the answer
        for k in range(i + 1, j + 1):
            if s[k] == first_letter:
                # Calculate turns by splitting the problem
                better_answer = self.Util(i, k - 1, s, dp) + self.Util(k + 1, j, s, dp)
                answer = min(answer, better_answer)

        # Store the result in the DP table
        dp[i][j] = answer
        
        # 04. Return the computed result
        return answer
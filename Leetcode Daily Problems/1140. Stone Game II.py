"""
01. Initialize Variables:
   - `n`: Length of the `piles` array.
   - `dp`: A 2D array where `dp[i][m]` represents the maximum stones Alice can get starting from index `i` with the current value of `M = m`.
   - `suffix_sum`: An array where `suffix_sum[i]` stores the sum of stones from index `i` to the end of the `piles` array.

02. Calculate Suffix Sum:
   - Fill the `suffix_sum` array by iterating from the second last element to the first element of the `piles` array.
   - `suffix_sum[i]` is calculated as the sum of `piles[i]` and `suffix_sum[i+1]`.

03. Dynamic Programming to Calculate Maximum Stones:
   - Iterate backward from the last pile to the first pile (from `i = n-1` to `i = 0`).
   - For each pile, iterate through possible values of `M`.
   - If taking all the remaining piles is possible (i.e., `i + 2 * m >= n`), set `dp[i][m]` to `suffix_sum[i]`.
   - Otherwise, calculate the maximum stones Alice can get by choosing an optimal number of piles `x`, where `1 <= x <= 2 * m`.
   - Update `dp[i][m]` as the maximum value between its current value and `suffix_sum[i] - dp[i + x][max(m, x)]`.

04. Return the Result:
   - The result is stored in `dp[0][1]`, which represents the maximum stones Alice can get starting from the first pile with `M = 1`.

Time Complexity: O(n^3), where n is the length of the `piles` array. The triple nested loops lead to cubic complexity.
Space Complexity: O(n^2), due to the 2D `dp` array and the `suffix_sum` array.
"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 01. Initialize variables
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]  # DP array
        suffix_sum = [0] * n  # Suffix sum array
        suffix_sum[-1] = piles[-1]  # Initialize the last element of suffix_sum
        
        # 02. Calculate the suffix sum
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # 03. Dynamic programming to calculate maximum stones Alice can get
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]  # Take all remaining piles
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])
        
        # 04. Return the maximum stones Alice can get starting with M = 1
        return dp[0][1]

'''
01. DP Array Initialization: Initialize a dynamic programming (DP) array `dp[c]`, where `c` represents the column index. This array will store the maximum score that can be achieved up to the current row by selecting the cell in column `c` of that row.

02. Row Transition Logic: For each row in the matrix, compute the maximum possible points for each column by evaluating two scenarios:
   - Moving from left to right: Use a `leftMax` array to track the highest values from previous columns while considering penalties for moving leftward.
   - Moving from right to left: Similarly, use a `rightMax` array to track the highest values from the opposite direction while accounting for penalties for moving rightward.

03. DP Array Update: Update the DP array for the current row by comparing the values from the `leftMax` and `rightMax` arrays and adjusting for penalties. This ensures that the DP array reflects the maximum possible score for each column in the current row.

Time Complexity: O(m × n), where `m` is the number of rows and `n` is the number of columns. The algorithm processes each cell only once.

Space Complexity: O(n), as only a single row of the DP array is maintained at any given time.
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        # Iterate through each row
        for i in range(1, m):
            leftMax = [0] * n
            rightMax = [0] * n
            newDp = [0] * n

            # Compute the max values from left to right
            leftMax[0] = dp[0]
            for j in range(1, n):
                leftMax[j] = max(leftMax[j - 1], dp[j] + j)

            # Compute the max values from right to left
            rightMax[n - 1] = dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                rightMax[j] = max(rightMax[j + 1], dp[j] - j)

            # Update the DP array for the current row
            for j in range(n):
                newDp[j] = max(leftMax[j] - j, rightMax[j] + j) + points[i][j]
            dp = newDp

        return max(dp)    
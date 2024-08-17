"""
01. Find Maximum Value: First, find the maximum value (`maxVal`) in the array `nums`.

02. Initialize Variables: 
   - `count`: Tracks how many times the maximum value appears in the current subarray.
   - `left`: Pointer to manage the left boundary of the sliding window.
   - `res`: Stores the count of subarrays that meet the condition.

03. Traverse the Array: Iterate through the array with a sliding window approach:
   - If the current element equals the maximum value (`maxVal`), increment the `count`.
   - While `count` is greater than or equal to `k`, adjust the window by moving the `left` pointer and decrementing `count` when necessary.
   - Add the value of `left` to `res`, which counts the valid subarrays.

04. Return the Result: After processing the entire array, return `res`, which contains the number of subarrays where the maximum element appears at least `k` times.

Time Complexity: O(n), where n is the length of the array. The array is traversed once.
Space Complexity: O(1), since only a constant amount of extra space is used.
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 01. Find the maximum value in the array
        maxVal = max(nums)
        
        # 02. Initialize variables
        count = 0  # Count of maximum value occurrences in the current window
        left = 0  # Left boundary of the sliding window
        res = 0  # Result to store the count of valid subarrays
        
        # 03. Traverse the array using a sliding window approach
        for right in range(len(nums)):  # Right boundary of the window
            if nums[right] == maxVal:
                count += 1  # Increment count if the current element is the maximum value
            
            # While the count of maxVal in the window is at least k
            while count >= k:
                if nums[left] == maxVal:
                    count -= 1  # Decrement count when moving the left boundary
                left += 1  # Move the left boundary to the right
            
            # Add the number of valid subarrays ending at the current position
            res += left
        
        # 04. Return the total count of valid subarrays
        return res
"""
01. Initialize Variables: 
   - `freq`: A dictionary to store the frequency of elements in the current subarray.
   - `n`: The length of the input array `nums`.
   - `ans`: To store the maximum length of a good subarray found so far.
   - `i` and `j`: Two pointers representing the sliding window boundaries.

02. Traverse the Array with Sliding Window: 
   - Expand the window by moving the `j` pointer and update the frequency of the current element in `freq`.
   - If the frequency of the current element exceeds `k`, shrink the window by moving the `i` pointer and adjust the frequency of the elements accordingly until the subarray becomes good again (i.e., all frequencies are less than or equal to `k`).

03. Update the Maximum Length: For every valid subarray (where all element frequencies are ≤ `k`), update `ans` with the maximum length of the subarray.

04. Return the Result: After traversing the entire array, return `ans`, which contains the length of the longest good subarray.

Time Complexity: O(n), where n is the length of the array. The sliding window ensures that each element is processed at most twice.
Space Complexity: O(n) due to the additional space used for the `freq` dictionary to store element frequencies.
"""

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # 01. Initialize variables
        freq = {}  # To track the frequency of elements in the current window
        n = len(nums)
        ans = 0  # To store the maximum length of a good subarray
        i = 0  # Left boundary of the sliding window
        
        # 02. Traverse the array using the sliding window technique
        for j in range(n):  # Right boundary of the sliding window
            # Increase the frequency of the current element
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            
            # If the frequency of any element exceeds k, shrink the window
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1  # Move the left boundary to the right
            
            # 03. Update the maximum length of a good subarray
            ans = max(ans, j - i + 1)
        
        # 04. Return the maximum length found
        return ans
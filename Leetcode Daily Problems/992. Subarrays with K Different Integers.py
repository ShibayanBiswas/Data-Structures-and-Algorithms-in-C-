"""
01. Use Helper Function for Subarrays with At Most K Distinct Integers: To find the number of subarrays with exactly `k` distinct integers, calculate the difference between the number of subarrays with at most `k` distinct integers and the number of subarrays with at most `k-1` distinct integers.

02. Initialize Variables in the Helper Function:
   - `ans`: To store the number of subarrays with at most `k` distinct integers.
   - `count`: An array to track the frequency of each integer in the current window.
   - `l`: Pointer to manage the left boundary of the sliding window.

03. Traverse the Array with Sliding Window:
   - Iterate through the array with the `r` pointer.
   - Increment the count of the current element.
   - If this is a new unique element in the window, decrement `k`.
   - If `k` becomes -1 (meaning there are more than `k` distinct integers), move the `l` pointer to reduce the number of distinct integers back to `k`.
   - Count the valid subarrays ending at the `r` pointer by adding `r - l + 1` to `ans`.

04. Calculate the Result: Return the difference between the number of subarrays with at most `k` distinct integers and the number of subarrays with at most `k-1` distinct integers.

Time Complexity: O(n), where n is the length of the array. The array is traversed twice with the sliding window technique.
Space Complexity: O(n), due to the additional space used for the `count` array.
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # 01. Calculate the result by finding the difference between subarrays with at most k distinct elements and at most k-1 distinct elements
        return self.subarraysWithAtMostKDistinct(nums, k) - self.subarraysWithAtMostKDistinct(nums, k - 1)
    
    def subarraysWithAtMostKDistinct(self, nums: List[int], k: int) -> int:
        # 02. Initialize variables
        ans = 0
        count = [0] * (len(nums) + 1)
        l = 0  # Left boundary of the sliding window
        
        # 03. Traverse the array with sliding window technique
        for r in range(len(nums)):  # Right boundary of the sliding window
            count[nums[r]] += 1
            
            # If this is a new unique element, reduce k
            if count[nums[r]] == 1:
                k -= 1
            
            # If there are more than k distinct elements, move the left pointer to reduce distinct count
            while k == -1:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            
            # Count the valid subarrays ending at r
            ans += r - l + 1
        
        # 04. Return the count of subarrays with at most k distinct elements
        return ans
"""
01. Handle Edge Case: If k is less than or equal to 1, return 0, because no positive product can be less than 1.

02. Initialize Variables: Set `product` to 1 to track the product of the current subarray. Initialize `result` to 0 to count the number of valid subarrays. Use `left` as the starting index of the sliding window.

03. Traverse the Array with Sliding Window: Iterate over the array with a `right` pointer:
   - Multiply the current number to the `product`.
   - If the `product` is greater than or equal to k, move the `left` pointer to reduce the product by dividing it by `nums[left]` and increment `left`.
   - Count all subarrays ending at `right` by adding `right - left + 1` to `result`.

04. Return the Result: After traversing the entire array, return `result` which contains the number of subarrays where the product is less than k.

Time Complexity: O(n), where n is the length of the array. The array is traversed once with the sliding window technique.
Space Complexity: O(1), since the solution uses constant extra space.
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 01. Handle the edge case where k <= 1
        if k <= 1:
            return 0
        
        # 02. Initialize variables
        product = 1
        result = 0
        left = 0
        
        # 03. Traverse the array with the sliding window technique
        for right, num in enumerate(nums):
            product *= num  # Multiply current number to the product
            
            # Shrink the window if the product is greater than or equal to k
            while product >= k:
                product /= nums[left]
                left += 1
            
            # Count all valid subarrays ending at 'right'
            result += right - left + 1
        
        # 04. Return the total count of valid subarrays
        return result
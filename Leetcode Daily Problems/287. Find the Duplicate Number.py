"""
01. Sort the Array: First, sort the array in ascending order. This will bring any duplicate numbers next to each other.

02. Traverse the Sorted Array: Iterate through the sorted array and check if any two consecutive elements are the same.
   - If a duplicate is found (i.e., `nums[i] == nums[i+1]`), return that number as the result.

03. Return Result: If no duplicate is found (though the problem guarantees one), return -1 as a fallback (this step is included for completeness but is not necessary in this problem).

Time Complexity: O(n log n) due to sorting the array.
Space Complexity: O(1) extra space, since the sorting is done in place (though technically O(n) due to the sorting algorithm's space requirements).
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 01. Sort the array
        nums.sort()
        
        # 02. Traverse the sorted array to find the duplicate
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:  # Check if consecutive elements are the same
                return nums[i]  # Return the duplicate number
        
        # 03. Return -1 if no duplicate is found (shouldn't happen per problem constraints)
        return -1
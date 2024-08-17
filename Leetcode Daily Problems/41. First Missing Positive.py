"""
01. Initialize Variables: Define a helper function `swap(arr, i, j)` to swap elements at indices `i` and `j` in the array `arr`. Get the length of the array `n`.

02. Place Elements in Their Correct Positions: Iterate through the array and for each element `nums[i]`, if it is a positive integer and lies in the range [1, n], place it in its correct position (i.e., `nums[i]` should be placed at index `nums[i] - 1`). Continue swapping until the element is either out of range or already in its correct position.

03. Find the First Missing Positive: After placing the elements in their correct positions, iterate through the array again. The first index `i` where `nums[i]` is not equal to `i + 1` indicates that `i + 1` is the smallest missing positive integer.

04. Return Result: If all positive integers from 1 to n are present, return `n + 1` as the smallest missing positive integer.

Time Complexity: O(n), where n is the number of elements in the array. The array is traversed twice, once for positioning the elements and once for finding the missing positive.
Space Complexity: O(1), as the algorithm modifies the array in place and uses only a constant amount of additional space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Function to swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)
        
        # 02. Place elements in their correct positions
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # 03. Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 04. Return result if all positive integers from 1 to n are present
        return n + 1
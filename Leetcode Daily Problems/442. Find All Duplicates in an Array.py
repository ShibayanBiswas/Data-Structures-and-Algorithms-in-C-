"""
01. Initialize the Duplicates List: Create an empty list `duplicates` to store the numbers that appear twice in the array.

02. Traverse the Array: Iterate through each number in the array `nums`.
   - Calculate the index by taking the absolute value of the current number and subtracting 1 (`index = abs(num) - 1`).
   - If the number at the calculated index is negative, it indicates that the number has already been encountered before, so add it to the `duplicates` list.
   - If the number at the calculated index is positive, negate the number at that index to mark it as visited.

03. Return the Duplicates List: After traversing the entire array, return the `duplicates` list containing all the numbers that appear twice.

Time Complexity: O(n), where n is the number of elements in the array. The array is traversed once.
Space Complexity: O(1) extra space, since the solution modifies the input array in place and uses only a constant amount of additional space.
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 01. Initialize the list to store duplicates
        duplicates = []
        
        # 02. Traverse the array to find duplicates
        for num in nums:
            index = abs(num) - 1  # Calculate the index based on the current number
            
            # Check if the number at the calculated index is negative
            if nums[index] < 0:
                duplicates.append(abs(num))  # The number is a duplicate
            else:
                # Negate the number at the calculated index to mark it as visited
                nums[index] = -nums[index]
        
        # 03. Return the list of duplicates
        return duplicates
'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''

'''

The approach we are following here is counting the number of zeros and moving all other number in the front and we just replace all the remaining positions as zero at the end.

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        
        pos = 0
        for i in nums:
            if i != 0:
                nums[pos] = i
                pos += 1
        
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0
        
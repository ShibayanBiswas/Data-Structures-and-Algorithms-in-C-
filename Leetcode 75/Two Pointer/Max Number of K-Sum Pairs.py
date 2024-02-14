'''

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

'''

'''

The intuition behind this solution is to use a two-pointer approach on a sorted array. Sorting the array allows us to efficiently find pairs of numbers that sum up to the target value k. The two pointers (left and right) are initialized at the beginning and end of the sorted array, and we move them towards each other based on the sum of the numbers at those positions.

'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0 
        right = len(nums) - 1
        operation = 0 

        while left < right:
            if ((nums[left] + nums[right]) == k):
                operation += 1
                left +=1 
                right -=1
                
            elif((nums[left] + nums[right]) < k):
                left += 1
                
            else:
                right -= 1
                
        return operation    
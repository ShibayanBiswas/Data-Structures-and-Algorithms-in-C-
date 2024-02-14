'''

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            # if n is less than f, it means n can be a potential candidate for the first element of an increasing triplet subsequence. So, it updates f to n
            if n <= first: 
                first = n
             # if n is greater than f and less than s, it means n can be a potential candidate for the second element of an increasing triplet subsequence. So, it updates s to n
            elif n <= second:
                second = n
             # if n is greater than both f and s, it indicates the presence of an increasing triplet subsequence. So, it returns True
            else:
                return True

        # if the loop completes without finding an increasing triplet subsequence, it means there is no such subsequence in the array, so it returns False
        return False
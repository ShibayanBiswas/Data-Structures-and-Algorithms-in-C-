'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

'''

'''
We use the fact that prefix_product of arr[i] is arr[0] * arr[1] * .. * arr[i-1] and postfix_product of arr[i] is arr[i+1] * arr[i+2] * .. * arr[n-1].

So basically, we have to calculate prefix_product * postfix_product[i] for each element.

1. Initialize a Solution Array of same size as input array with value.
2. Store Prefix and Postfix Product so far in variables.
3. Traverse the input array.
4. Before updating the values for each i, multiply current solution array value at i with the value of prefix i.e. multiply with prefix product of the previous i-1 elements.
5. Similarly, calculate the postfix product value for n-i-1 where n is length of input array at each iteration.
6. As in Step 4, before calculating the postfix for i'th value , multiply the solution_array[n-i-1] with the postfix product value i.e. products of input[i+1] to input[n-1].

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        solution = [1] * length
        prefix = 1
        postfix = 1

        for i in range(length):
            solution[i] *= prefix
            prefix *= nums[i]

            solution[length-i-1] *= postfix
            postfix *= nums[length-i-1]

        return(solution)
        
        
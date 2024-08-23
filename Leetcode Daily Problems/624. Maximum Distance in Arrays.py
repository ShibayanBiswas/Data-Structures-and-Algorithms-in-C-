'''
01. Initialize Variables: Set min_value to a large number (e.g., float('inf')) and max_value to a small number (e.g., -float('inf')). Start with max_diff initialized to 0. 

02. Single Pass Through Arrays: Iterate through each array in arrays. For each array, extract the first (first_element) and last (last_element) elements. Update max_diff by comparing the difference between the largest element encountered so far and the current array's first element, as well as the difference between the smallest element encountered so far and the current array's last element. After checking the differences, update min_value with the smallest element found so far and max_value with the largest element.

03. Update min and max: After checking the differences, update min_value with the smallest element found so far and max_value with the largest element.

Time Complexity: O(n), where n is the number of arrays. We only iterate through each array once.
Space Complexity: O(1), as only a constant amount of additional space is used.
'''

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value, max_value = float('inf'), -float('inf')
        max_diff = 0
        
        for arr in arrays:
            first_element, last_element = arr[0], arr[-1]
            max_diff = max(max_diff, last_element - min_value, max_value - first_element)
            min_value = min(min_value, first_element)
            max_value = max(max_value, last_element)
            
        return max_diff
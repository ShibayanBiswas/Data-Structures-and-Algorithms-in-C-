"""
01. Initialize a List to Store Values: Create an empty list `list_vals` to store the values of the linked list nodes as you traverse through the list.

02. Traverse the List: Iterate through the linked list, appending each node's value to the `list_vals` list. Continue until the end of the list is reached.

03. Check for Palindrome: Use two pointers, `left` starting from the beginning of the list and `right` starting from the end. Compare the values at these two pointers:
   - If the values are the same, move the `left` pointer forward and the `right` pointer backward.
   - Continue this process until the `left` pointer meets or crosses the `right` pointer.

04. Return the Result: If all corresponding values from the start and end match, return `True` (indicating the list is a palindrome). Otherwise, return `False`.

Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list twice: once to collect values and once to check for palindrome.
Space Complexity: O(n), since we're storing the list values in a separate list.
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize a list to store the node values
        list_vals = []
        
        # Traverse the list and collect the values
        while head:
            list_vals.append(head.val)
            head = head.next
        
        # Check if the list is a palindrome using two pointers
        left, right = 0, len(list_vals) - 1
        while left < right:
            if list_vals[left] != list_vals[right]:
                return False  # Not a palindrome
            left += 1
            right -= 1
        
        # If all corresponding values match, it's a palindrome
        return True
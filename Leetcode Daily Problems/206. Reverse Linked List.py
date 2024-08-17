"""
01. Initialize Variables: Set `temp` to the head of the linked list, `prev` to `None`, and `front` to `None`. These variables will help in reversing the pointers in the list.

02. Traverse the List: While `temp` (the current node) is not `None`, perform the following steps:
   - Store the next node in `front` (`front = temp.next`).
   - Reverse the current node's pointer by setting `temp.next` to `prev`.
   - Move the `prev` pointer to the current node (`prev = temp`).
   - Move the `temp` pointer to the next node (`temp = front`).

03. Return the Reversed List: After the loop completes, `prev` will point to the new head of the reversed list. Return `prev` as the result.

Time Complexity: O(n), where n is the number of nodes in the linked list. We only traverse the list once.
Space Complexity: O(1), as only a constant amount of additional space is used.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize variables
        current = head
        previous = None
        
        # Traverse through the list
        while current is not None:
            next_node = current.next  # Save the next node
            current.next = previous   # Reverse the link
            previous = current        # Move the previous pointer forward
            current = next_node       # Move the current pointer forward
        
        # Return the new head of the reversed list
        return previous
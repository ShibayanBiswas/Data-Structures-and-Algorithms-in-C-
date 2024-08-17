"""
01. Find the Middle of the List: Use the slow and fast pointer technique to find the middle node of the linked list. 
   - `slow` moves one step at a time, while `fast` moves two steps at a time. When `fast` reaches the end, `slow` will be at the middle.

02. Reverse the Second Half of the List: Once the middle is found, reverse the second half of the list starting from the middle.
   - Initialize `prev` to `None` and `curr` to the middle node (`slow`). Traverse through the second half, reversing the pointers as you go.

03. Merge the Two Halves: After reversing the second half, merge the first half and the reversed second half.
   - Start with the head of the first half and the head of the reversed second half, alternately linking nodes from each half.

Time Complexity: O(n), where n is the number of nodes in the linked list. The list is traversed multiple times but still in linear time.
Space Complexity: O(1), as the reordering is done in-place without using extra space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Check if the list is empty or has only one node
        if not head:
            return 
        
        # 01. Find the middle of the list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 02. Reverse the second half of the list starting from the middle
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # 03. Merge the two halves of the list
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
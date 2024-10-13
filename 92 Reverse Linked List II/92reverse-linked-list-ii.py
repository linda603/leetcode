# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # handle the head of the new list easily
        
        left_prev = dummy
        # shift left_prev l - 1 time to make left_prev at the node just before left node
        for i in range(left - 1):
            left_prev = left_prev.next

        prev = None
        curr = left_prev.next
        # reverse r - l + 1 time
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # correct the last 2 links from left_prev.next.next (Example 1: 2.next = NULL)
        #                               left_prev.next (Example 1: 1.next = 2)
        left_prev.next.next = curr
        left_prev.next = prev
        
        return dummy.next

# Time: O(n)
# Space: O(1)
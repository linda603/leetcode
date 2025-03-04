# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_left = dummy

        for i in range(left - 1):
            prev_left = prev_left.next

        # Reverse from left to right
        curr = prev_left.next
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # Correct prev_left pointer and tail pointer
        prev_left.next.next = curr
        prev_left.next = prev
        return dummy.next

# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = second = head
        for i in range(k - 1):
            first = first.next
        
        curr = first
        while curr.next:
            second = second.next
            curr = curr.next
        first.val, second.val = second.val, first.val
        return head

# Time: O(n)
# Space: O(1)

# 1 -> 2 -> 3 -> 4 -> 5
#     first
#                    curr
#              second
                    
     
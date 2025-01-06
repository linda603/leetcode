# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        prev = head
        curr = head.next

        while curr:
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            tmp = dummy
            while curr.val > tmp.next.val:
                tmp = tmp.next
            
            # assign prev.next to save the next curr
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr

            curr = prev.next 
        return dummy.next

# Time: O(n) best case, O(n^2) worst case
# Space: O(1)

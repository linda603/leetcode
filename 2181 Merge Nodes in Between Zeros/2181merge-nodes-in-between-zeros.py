# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head.next
        curr = head.next.next

        while curr:
            while curr.val != 0:
                tail.val += curr.val
                curr = curr.next
            tail.next = curr.next
            tail = tail.next
            if curr.next:
                curr = curr.next.next
            else:
                break
        return head.next

#Time: O(n)
#Space: O(1)
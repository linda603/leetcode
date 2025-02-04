# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = self.reverse(slow.next)
        slow.next = None
        first = head
        res = 0

        while first and second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next
        return res
    
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

# Time: O(n/2 + n/2 + n/2) = O(n)
# Space: O(1)

        
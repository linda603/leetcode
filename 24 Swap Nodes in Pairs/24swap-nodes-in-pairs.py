# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            # save next pair and second node
            next_pair = curr.next.next
            second = curr.next

            # correct pointers of curr pair
            prev.next = second
            second.next = curr
            curr.next = next_pair

            # update prev and curr
            prev = curr
            curr = next_pair
        return dummy.next

# Time: O(n)
# Space: O(1)
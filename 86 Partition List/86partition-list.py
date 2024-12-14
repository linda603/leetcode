# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0, None) # small list has smaller val < x
        small_tail = small
        large = ListNode(0, None) # large list has greater val > x
        large_tail = large

        curr = head
        while curr:
            if curr.val < x:
                small_tail.next = curr
                small_tail = small_tail.next
            else:
                large_tail.next = curr
                large_tail = large_tail.next
            curr = curr.next
        
        # merge left and right lists
        small_tail.next = large.next
        large_tail.next = None
        return small.next

# Time: O(n)
# Space: O(1)
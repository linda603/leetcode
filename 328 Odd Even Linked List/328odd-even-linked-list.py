# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution2: Link changes
        # head = [2,    1,   3,5,6,4,7]
        #         odd   even odd
        #               evenHead
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = evenHead
        return head

#Time: O(n)
#Space: O(1)
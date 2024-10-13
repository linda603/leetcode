# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy

        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                # move curr pointer to the end of duplicated nodes list
                # delete duplicated nodes by moving tail.next = curr.next
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                tail.next = curr.next
            else:
                tail = tail.next
            curr = curr.next
        
        return dummy.next

# Time: O(n)
# Space: O(1)
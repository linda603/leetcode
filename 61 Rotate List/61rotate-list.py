# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        length, tail = self.get_length(head)
        print(length, tail.val)
        k = k % length
        if not k: return head

        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        
        return new_head
    
    def get_length(self, head):
        length = 1
        curr = head
        
        while curr.next:
            curr = curr.next
            length += 1
        return [length, curr]

# Time: O(n)
# Space: O(1)
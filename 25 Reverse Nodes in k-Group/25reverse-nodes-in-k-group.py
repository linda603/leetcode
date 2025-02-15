# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        curr = head

        while True:
            k_node = self.get_k_node(prev_group, k)
            if not k_node:
                break
            next_group = k_node.next
            prev = next_group
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # correct pointers
            tmp = prev_group.next
            prev_group.next = k_node
            prev_group = tmp

            curr = next_group
        return dummy.next
    
    def get_k_node(self, head, k):
        
        while head and k:
            head = head.next
            k -= 1
        return head

# Time: O(2n)
# Space: O(1)
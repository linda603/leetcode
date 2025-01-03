# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            k_node = self.get_k_node(prev_group, k)
            if not k_node:
                break
            next_group = k_node.next

            curr = prev_group.next
            prev = k_node.next
            self.reverse(curr, prev, k)

            tmp = prev_group.next
            prev_group.next = k_node
            prev_group = tmp
            curr.next = next_group
        return dummy.next

    def get_k_node(self, node, k):
        curr = node

        while k and curr:
            curr = curr.next
            k -= 1
        return curr
    
    def reverse(self, curr, prev, k):

        while k and curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            k -= 1
        return prev

# Time: O(2n)
# Space: O(1)

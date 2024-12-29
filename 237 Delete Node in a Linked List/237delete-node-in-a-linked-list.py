# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1. node is not a tail node. Copy the next node val to curr node
        node.val = node.next.val
        # 2. Delete the next node sice curr node & next node have the same vals
        node.next = node.next.next

# Time: O(1)
# Space: O(1)
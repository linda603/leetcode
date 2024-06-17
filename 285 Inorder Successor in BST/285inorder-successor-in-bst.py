# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        curr = root

        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                successor = curr
                curr = curr.left
        
        return successor

#Time: O(n)
#Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first_violation = None
        self.second_violation = None
        self.prev = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        tmp = self.first_violation.val
        self.first_violation.val = self.second_violation.val
        self.second_violation.val = tmp
    
    # inorder traversal
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        # processing at curr node, check is violation happens
        if self.prev and node.val < self.prev.val:
            if not self.first_violation:
                self.first_violation = self.prev
            self.second_violation = node
        self.prev = node
        self.dfs(node.right)

# Time: O(n)
# Space: O(h)
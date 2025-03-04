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
        self.first_violation.val, self.second_violation.val = self.second_violation.val, self.first_violation.val

    def dfs(self, node):
        if not node:
            return
        left = self.dfs(node.left)
        if self.prev and self.prev.val > node.val:
            if not self.first_violation:
                self.first_violation = self.prev
            self.second_violation = node
        self.prev = node
        right = self.dfs(node.right)

# Time: O(n)
# Space: O(h)
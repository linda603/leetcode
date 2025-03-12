# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)
    
    def dfs(self, node, low, high):
        if not node:
            return 0
        left = self.dfs(node.left, low, high)
        right = self.dfs(node.right, low, high)
        if low <= node.val <= high:
            return left + right + node.val
        return left + right

# Time: O(n)
# Space: O(h)
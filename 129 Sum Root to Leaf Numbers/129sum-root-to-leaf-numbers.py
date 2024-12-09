# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, total):
            if not node:
                return 0
            total = total * 10 + node.val
            left = dfs(node.left, total)
            right = dfs(node.right, total)
            if not node.left and not node.right:
                return total
            return left + right
        
        return dfs(root, 0)

# Time: O(n)
# Space: O(h)
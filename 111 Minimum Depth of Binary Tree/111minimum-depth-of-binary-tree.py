# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float("inf")
        
        def dfs(node, level):
            nonlocal res
            if not node:
                return
            # leaf node
            if not node.left and not node.right:
                res = min(res, level)
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return
        dfs(root, 1)
        return res

# Time: O(n)
# Space: O(h)
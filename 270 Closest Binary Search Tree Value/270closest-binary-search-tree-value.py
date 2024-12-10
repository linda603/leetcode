# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if abs(node.val - target) < abs(res - target):
                res = node.val
            elif abs(node.val - target) == abs(res - target):
                res = min(res, node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return res

# Time: O(n)
# Space: O(h)
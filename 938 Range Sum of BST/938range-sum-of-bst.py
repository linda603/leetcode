# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            if node.val >= low and node.val <= high:
                res += node.val
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return res

# Time: O(n)
# Space: O(h)
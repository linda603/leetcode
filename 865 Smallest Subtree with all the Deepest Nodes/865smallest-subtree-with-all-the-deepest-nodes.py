# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = root
        max_depth = 0

        def dfs(node, level):
            nonlocal res, max_depth
            if not node:
                return level
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            if left == right:
                max_depth = max(max_depth, left)
                if max_depth == left:
                    res = node
                return left
            return max(left, right)
    
        dfs(root, 0)
        return res

# Time: O(n)
# Space: O(h)
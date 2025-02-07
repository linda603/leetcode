# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            count = dfs(node.left)
            count += dfs(node.right)
            if node == p or node == q:
                count += 1
            if count == 2:
                res = node
                count = 0
            return count
        dfs(root)
        return res

# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, go_left):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right:
                if go_left:
                    res += node.val
                return
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return res

# Time: O(n)
# Space: O(h)
            
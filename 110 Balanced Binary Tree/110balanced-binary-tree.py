# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [0, True] # [depth, is_balanced]
            left = dfs(node.left)
            right = dfs(node.right)
            depth = 1 + max(left[0], right[0])
            is_balanced = left[1] and right[1] and (abs(left[0] - right[0]) <= 1)
            return [depth, is_balanced]
        return dfs(root)[1]

# Time: O(n)
# Space: O(h)
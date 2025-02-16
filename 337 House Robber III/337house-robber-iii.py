# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])
    
    def dfs(self, node):
        if not node:
            return [0, 0]
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        max_with_node = node.val + left[1] + right[1]
        max_without_node = max(left[0], left[1]) + max(right[0], right[1])
        return [max_with_node, max_without_node]

# Time: O(n)
# Space: O(h)

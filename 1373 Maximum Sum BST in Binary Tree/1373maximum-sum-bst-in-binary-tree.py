# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = self.dfs(root)[0]
        return res if res > 0 else 0
    
    def dfs(self, node):
        if not node:
            return [0, float("inf"), float("-inf")]
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left[2] < node.val and node.val < right[1]:
            return [left[0] + right[0] + node.val, min(left[1], node.val), max(right[2], node.val)]
        return [max(left[0], right[0]), float("-inf"), float("inf")]

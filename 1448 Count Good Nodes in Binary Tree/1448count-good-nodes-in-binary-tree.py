# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, prev):
            if not node:
                return 0
            res = 0
            if node.val >= prev:
                res += 1
                prev = node.val
            return res + dfs(node.left, prev) + dfs(node.right, prev)
        
        return dfs(root, float("-inf"))

#Time: O(n)
#Space: O(h)
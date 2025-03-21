# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = float("inf")

        def dfs(node):
            nonlocal prev, res
            if not node:
                return
            dfs(node.left)
            if prev:
                res = min(res, node.val - prev.val)
                
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res

#Time: O(n)
#Space: O(h), worst case O(n)
        
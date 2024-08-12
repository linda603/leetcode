# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                return
            res.append("(")
            res.append(str(node.val))
            if not node.left and node.right:
                res.append("()")
            dfs(node.left)
            dfs(node.right)
            res.append(")")
        
        dfs(root)
        return "".join(res[1:-1])

#Time: O(n)
#Space: O(h)
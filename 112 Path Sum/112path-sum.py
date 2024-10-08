# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, total):
            if not node:
                return False
            total += node.val
            # only return True if node is the leaf node and total == targetSum
            if not node.left and not node.right and total == targetSum:
                return True

            return dfs(node.left, total) or dfs(node.right, total)
        
        return dfs(root, 0)

#Time: O(n)
#Space: O(h)
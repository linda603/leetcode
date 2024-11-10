# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        res = 0

        def dfs(node, depth):
            nonlocal res, max_depth
            if not node.left and not node.right:
                if depth == max_depth:
                    res += node.val
                elif depth > max_depth:
                    res = node.val
                    max_depth = depth
                return
            if node.left: dfs(node.left, depth + 1)
            if node.right: dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res

# Time: O(n)
# Space: O(h). Worst case: O(n)
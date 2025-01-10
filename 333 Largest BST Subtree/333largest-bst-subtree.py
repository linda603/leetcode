# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [float("inf"), float("-inf"), 0] # min val, max val, total nodes
            left = dfs(node.left)
            right = dfs(node.right)
            # valid bst if largest left subtree < node.val < smallest right subtree
            if left[1] < node.val < right[0]:
                return [min(left[0], node.val), max(right[1], node.val), left[2] + right[2] + 1]
            else:
                return [float("-inf"), float("inf"), max(left[2], right[2])]
        
        return dfs(root)[2]

# Time: O(n)
# Space: O(h)
            


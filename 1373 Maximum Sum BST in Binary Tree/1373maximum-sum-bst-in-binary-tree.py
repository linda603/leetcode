# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return [0, float("inf"), float("-inf")] # [size, min, max]
            left = dfs(node.left)
            right = dfs(node.right)

            # not valid BST
            if not (left[2] < node.val < right[1]):
                return [0, float("-inf"), float("inf")] # so that parent cannot be a BST
            curr_sum = left[0] + node.val + right[0]
            res = max(res, curr_sum)
            return [curr_sum, min(node.val, left[1]), max(node.val, right[2])]
        
        dfs(root)
        return res

# Time: O(n) for post order traversal
# Space: O(h). h: height of the binary tree
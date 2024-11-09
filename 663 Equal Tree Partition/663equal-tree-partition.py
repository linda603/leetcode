# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        total_sum = self.sum_tree(root)
        if total_sum % 2: return False

        half = total_sum // 2
        return self.dfs(root.left, half)[1] or self.dfs(root.right, half)[1]
    
    def sum_tree(self, node):
        if not node:
            return 0
        return node.val + self.sum_tree(node.left) + self.sum_tree(node.right)
    
    def dfs(self, node, target):
        if not node:
            return [0, False]
        left = self.dfs(node.left, target)
        right = self.dfs(node.right, target)

        curr_sum = node.val + left[0] + right[0]
        is_valid = left[1] or right[1] or curr_sum == target
        return [curr_sum, is_valid]

# Time: O(n + n) = O(n)
# Space: O(h + h) = O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            res = []
            res += dfs(node.left)
            res += dfs(node.right)
            return res

        arr1 = dfs(root1)
        arr2 = dfs(root2)

        return arr1 == arr2

# Time: O(n1 + n2)
# Space: O(n1 + n2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, isLeft, depth):
            if not node:
                return 0
            if isLeft: #Previously the tree goes left
                right = dfs(node.right, False, depth + 1)
                left = dfs(node.left, True, 1) # Reset the depth if we continue going left
            else:
                left = dfs(node.left, True, depth + 1)
                right = dfs(node.right, False, 1)
            depth = max(left, right, depth)
            return depth
        
        return max(dfs(root, True, 0), dfs(root, False, 0))

#Time: O(n)
#Space: O(h)

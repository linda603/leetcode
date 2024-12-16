# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Identify 1st violation. first = prev, second = curr (in case don't have 2nd violation, still can swap first & second)
        #.            2nd violation. second = curr
        # swap first and second
        first = None
        second = None
        prev = None

        # inorder traversal
        def dfs(node):
            nonlocal first, second, prev
            if not node:
                return
            dfs(node.left)
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node
            dfs(node.right)
    
        dfs(root)
        if first and second:
            first.val, second.val = second.val, first.val
        return root

# Time: O(n)
# Space: O(h)

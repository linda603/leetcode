# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root

        # root = [1, 2, 3, 4, null, 6]
        while curr:
            if curr.left:
                # curr = 1, go until tail = 4
                tail = curr.left
                while tail.right:
                    tail = tail.right
                
                # correct the pointers, 4 -> 5, 1 - > 2
                tail.right = curr.right
                curr.right = curr.left
                # remove curr left children
                curr.left = None
            curr = curr.right
        
# Time: O(2n)
# Space: O(1)
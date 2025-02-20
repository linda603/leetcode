# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        curr = root

        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val, None, None)
                    break
                curr = curr.left
            elif val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val, None, None)
                    break
                curr = curr.right
        return root

# Time: O(logn)
# Space: O(1)
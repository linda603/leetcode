# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        while curr:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

#Time: O(logn)
#Space: O(1)
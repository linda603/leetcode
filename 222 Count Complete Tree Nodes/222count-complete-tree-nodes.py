# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.get_height(root, True)
        right_height = self.get_height(root, False)
        print("root.val, left_height, right_height:", root.val, left_height, right_height)

        if left_height == right_height:
            return 2 ** left_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def get_height(self, node, left):
        res = 0

        while node:
            res += 1
            if left:
                node = node.left
            else:
                node = node.right
        return res

#Time: O(h^2) = O((logn)^2)
#Space: O(h) = O(logn)
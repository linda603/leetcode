# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        right = []

        def is_leaf(node):
            return not node.left and not node.right
        
        def get_left_bound(node):
            nonlocal res
            if not node or is_leaf(node):
                return
            
            res.append(node.val)
            if node.left:
                get_left_bound(node.left)
            else:
                get_left_bound(node.right)
            return
        
        def get_leaf(node):
            nonlocal res
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            get_leaf(node.left)
            get_leaf(node.right)
            return
        
        def get_right_bound(node):
            nonlocal right
            if not node or is_leaf(node):
                return
            right.append(node.val)
            if node.right:
                get_right_bound(node.right)
            else:
                get_right_bound(node.left)
            return
        
        if is_leaf(root):
            return [root.val]

        res.append(root.val)
        get_left_bound(root.left)
        get_leaf(root)
        get_right_bound(root.right)

        while right:
            res.append(right.pop())

        return res

# Time: O(h + n + h + h) = O(n)
# Space: O(n)
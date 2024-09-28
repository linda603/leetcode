# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)   
    
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

#Time: O(m*n). m: nodes in root, n: nodes in subRoot
#       For every m node in root, we check if the tree root is identical to subRoot
#Space: O(m+n). m: dfs(isSubtree), n: dfs(is_same_tree)
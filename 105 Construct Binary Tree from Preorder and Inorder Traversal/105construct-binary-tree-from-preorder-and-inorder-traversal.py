# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_i = 0

        def dfs(l, r):
            nonlocal preorder_i
            if l > r:
                return None
            
            root = TreeNode(preorder[preorder_i])
            preorder_i += 1
            root.left = dfs(l, inorder_map[root.val] - 1)
            root.right = dfs(inorder_map[root.val] + 1, r)
            return root
        
        return dfs(0, len(inorder) - 1)

#Time: O(n)
#Space: O(n)
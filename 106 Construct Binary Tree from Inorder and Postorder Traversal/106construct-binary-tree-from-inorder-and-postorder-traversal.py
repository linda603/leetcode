# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def dfs(l , r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            i = inorder_map[root.val]
            root.right = dfs(i + 1, r)
            root.left = dfs(l, i - 1)
            return root

        return dfs(0, len(inorder) - 1)

#Time: O(n)
#Space: O(n)
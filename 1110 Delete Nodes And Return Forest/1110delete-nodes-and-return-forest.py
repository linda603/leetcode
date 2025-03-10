# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        self.dfs(root, delete_set)
        if root.val not in delete_set:
            self.res.append(root)
        return self.res

    def dfs(self, node, to_delete):
        if not node:
            return False
        left = self.dfs(node.left, to_delete)
        right = self.dfs(node.right, to_delete)
        if node.val in to_delete:
            if not left and node.left:
                self.res.append(node.left)
            if not right and node.right:
                self.res.append(node.right)
            return True
        if left:
            node.left = None
        if right:
            node.right = None
        return False

# Time: O(n)
# Space: O(h)
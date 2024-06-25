# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        remaining = []

        def removeNodes(root, remaining):
            if not root:
                return None
            root.left = removeNodes(root.left, remaining)
            root.right = removeNodes(root.right, remaining)

            if root.val in toDelete:
                if root.left:
                    remaining.append(root.left)
                if root.right:
                    remaining.append(root.right)
                return None
            return root

        removeNodes(root, remaining)

        if root.val not in toDelete:
            remaining.append(root)

        return remaining

#Time: O(n) n: number of nodes in the tree
#Space: O(h + m) = O(h) due to dfs() calls, worst case O(n), m: hash set size
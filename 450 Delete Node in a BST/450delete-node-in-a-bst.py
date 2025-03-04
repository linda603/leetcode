# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            return self.remove_node(root)
        curr = root

        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.remove_node(curr.left)
                    break
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.remove_node(curr.right)
                    break
                curr = curr.right
        return root

    def remove_node(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        most_right = self.find_most_right(node.left)
        most_right.right = node.right
        return node.left

    def find_most_right(self, node):
        curr = node

        while curr.right:
            curr = curr.right
        return curr

# Time: O(logn)
# Space: O(1)
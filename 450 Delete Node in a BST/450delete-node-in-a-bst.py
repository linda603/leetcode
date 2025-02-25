# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            return self.remove_node(root)
    
        curr = root
        while curr:
            # if the node is found, correct the pointers
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = self.remove_node(curr.left)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.remove_node(curr.right)
                    break
                else:
                    curr = curr.right
        return root

    def remove_node(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # find the most right of left child tree
        most_right = self.find_most_right(node.left)
        # every node in the right child is greater than left child
        most_right.right = node.right
        return node.left
    
    def find_most_right(self, node):
        curr = node
        while curr.right:
            curr = curr.right
        return curr

# Time: O(h) = O(logn)
# Space: O(1)
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
    
    def find_most_left(self, node):
        curr = node

        while curr.left:
            curr = curr.left
        return curr

    def remove_node(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
  
        # Find the most left (smallest element in the right sub tree)
        most_left = self.find_most_left(node.right)
        # every node in the left subtree is smaller than the right subtree
        most_left.left = node.left
        return node.right
    

# Time: O(h) = O(logn) to find node has key val + find most left node
# Space: O(1)
                

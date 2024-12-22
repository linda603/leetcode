# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()
        curr = top.right

        while curr:
            self.stack.append(curr)
            curr = curr.left
        return top.val

    def hasNext(self) -> bool:
        return True if self.stack else False

# Time: instructor() O(h), next(): O(1) average, O(h) worst case, hasNext O(1)
# Space: O(h)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        if root:
            queue.append(root)
        
        even = True
        while queue:
            prev = float("-inf") if even else float("inf")
            for i in range(len(queue)):
                node = queue.popleft()
                if (even and (not node.val % 2 or prev >= node.val)) or (not even and (node.val % 2 or prev <= node.val)):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
            even = not even
        return True

# Time: O(n)
# Space: O(n)
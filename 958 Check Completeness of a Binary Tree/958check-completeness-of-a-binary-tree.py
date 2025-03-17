# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        if root:
            queue.append(root) # N, 7, N, N, N, N

        while queue:
            node = queue.popleft()
            if not node:
                for i in range(len(queue)):
                    if queue.popleft():
                        return False
                break
            queue.append(node.left)
            queue.append(node.right)
    
        return True
    
# T: O(n)
# S: O(n)
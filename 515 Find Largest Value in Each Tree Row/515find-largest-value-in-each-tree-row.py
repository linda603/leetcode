# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            max_val = float("-inf")    
            for _ in range(size):
                node = queue.popleft()
                max_val = max(max_val, node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            
            res.append(max_val)
        
        return res
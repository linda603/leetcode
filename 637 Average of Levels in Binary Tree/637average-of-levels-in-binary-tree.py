# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while queue:
            len_q = len(queue)
            total = 0
            for i in range(len_q):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(total / len_q)

        return res

# Time: O(n)
# Space: O(h)
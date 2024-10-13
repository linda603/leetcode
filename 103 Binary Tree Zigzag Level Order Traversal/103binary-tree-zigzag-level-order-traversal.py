# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        if root:
            queue.append(root)
        res = []

        reverse = False
        while queue:
            len_q = len(queue)
            level = []
            for i in range(len_q):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse: 
                level = level[::-1]
            res.append(level)
            reverse = not reverse

        return res

# Time: O(n)
# Space: O(n)
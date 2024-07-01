# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float("-inf")
        level = 0
        res = 0

        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            qLen = len(queue)
            curr = 0
            for i in range(qLen):
                node = queue.popleft()
                curr += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            if curr > maxVal:
                maxVal = curr
                res = level
        return res

#Time: O(n)
#Space: O(n)
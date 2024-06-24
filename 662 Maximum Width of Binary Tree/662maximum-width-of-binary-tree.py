# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([[root, 1, 0]]) #[node, number, level]

        preLevel = 0
        preNum = 1

        while queue:
            node, num, level = queue.popleft()

            if level > preLevel:
                preLevel = level
                preNum = num
            newWidth = num - preNum + 1
            res = max(res, newWidth)

            if node.left:
                queue.append([node.left, num * 2, level + 1])
            if node.right:
                queue.append([node.right, num * 2 + 1, level + 1])
        return res
        
#Time: O(n)
#Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.time = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.dfs(root, start)
        return self.time
        
    def dfs(self, node, start):
        if not node:
            return [False, 0] # [found start node, depth from this node]
        left = self.dfs(node.left, start)
        right = self.dfs(node.right, start)

        if node.val == start:
            self.time = max(self.time, max(left[1], right[1]))
            return [True, 1]
        if left[0]:
            self.time = max(self.time, left[1] + right[1])
            return [True, 1 + left[1]]
        elif right[0]:
            self.time = max(self.time, left[1] + right[1])
            return [True, 1 + right[1]]
        else:
            return [False, 1 + max(left[1], right[1])] # [False, max_depth from this node to leaf node from left child + right child]

# Time: O(n)
# Space: O(1)
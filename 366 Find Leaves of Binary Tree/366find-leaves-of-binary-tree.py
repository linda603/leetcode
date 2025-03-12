# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        heights = []
        self.dfs(root, heights)
        return heights

    def dfs(self, node, heights):
        if not node:
            return -1 # height of the Null node
        curr_height = max(self.dfs(node.left, heights), self.dfs(node.right, heights)) + 1
        if curr_height == len(heights):
            heights.append([])
        heights[curr_height].append(node.val)
        return curr_height

# Time: O(n)
# Space: O(n)
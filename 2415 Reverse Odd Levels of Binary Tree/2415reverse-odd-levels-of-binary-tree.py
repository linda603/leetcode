# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS level traversal
        queue = collections.deque()
        if root:
            queue.append(root)

        level = 0
        while queue:
            size = len(queue)
            curr = []
            for i in range(size):
                node = queue.popleft()
                curr.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2:
                self.reverse(curr)
            level += 1
        return root
    
    def reverse(self, arr):
        l = 0
        r = len(arr) - 1

        while l < r:
            arr[l].val, arr[r].val = arr[r].val, arr[l].val
            l += 1
            r -= 1
        return

# Time: O(n)
# Space: O(n)
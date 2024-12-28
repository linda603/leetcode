# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        cols = defaultdict(list) # col: [node]
        queue = deque([(root, 0)]) # (node, vertical col)
        min_c = float("inf")
        max_c = float("-inf")

        while queue:
            node, c = queue.popleft()
            cols[c].append(node.val)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
            if node.left:
                queue.append((node.left, c - 1))
            if node.right:
                queue.append((node.right, c + 1))

        res = []
        for c in range(min_c, max_c + 1):
            res.append(cols[c])
        return res

# Time: O(n + n) = O(n)
# Space: O(h + n) = O(n)
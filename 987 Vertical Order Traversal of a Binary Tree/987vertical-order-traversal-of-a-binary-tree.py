# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols_map = {}
        # 0: 1, 15
        # -1: 9
        # 1: 20

        queue = deque([(root, 0)])
        min_col = 0
        max_col = 0

        level = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, col = queue.popleft()
                if col not in cols_map:
                    cols_map[col] = defaultdict(list)
                cols_map[col][level].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
                min_col = min(min_col, col)
                max_col = max(max_col, col)
            level += 1
        
        res = []
        for col in range(min_col, max_col + 1):
            curr_list = []
            for curr_level in range(0, level + 1):
                if curr_level in cols_map[col]:
                    for val in sorted(cols_map[col][curr_level]):
                        curr_list.append(val)
            res.append(curr_list)
        return res

# Time: O(n + ?)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        parents = self.get_parent(root)

        queue = collections.deque([target])
        visited = set()

        while queue and k >= 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if k == 0:
                    res.append(node.val)
                visited.add(node)
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if node in parents and parents[node] not in visited:
                    queue.append(parents[node])
            k -= 1
        return res
    
    def get_parent(self, root):
        parents = {}
        queue = collections.deque()
        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    parents[node.left] = node
                if node.right:
                    queue.append(node.right)
                    parents[node.right] = node
        return parents

# Time: O(n + n)
# Space: O(n) due to parents map + res
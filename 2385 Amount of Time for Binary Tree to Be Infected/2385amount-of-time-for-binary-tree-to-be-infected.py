# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        parent_map, start_node = self.get_parents(root, start)

        # bfs
        time = 0
        queue = deque([start_node])
        visited = set()

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                visited.add(node)
                if node in parent_map and parent_map[node] not in visited:
                    queue.append(parent_map[node])
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
            time += 1
        return time - 1
    
    def get_parents(self, root, start):
        parent_map = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.val == start:
                start_node = node
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)
        return (parent_map, start_node)
            
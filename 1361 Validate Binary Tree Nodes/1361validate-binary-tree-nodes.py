class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = self.find_root(n, leftChild, rightChild)
        if root == -1:
            return False
        
        adj = self.get_adj(n, leftChild, rightChild)
        visited = set()
        if not self.dfs(adj, root, visited):
            return False

        return True if len(visited) == n else False
    
    def find_root(self, n, leftChild, rightChild):
        left_child_set = set(leftChild)
        right_child_set = set(rightChild)

        for i in range(n):
            if i not in left_child_set and i not in right_child_set:
                return i
        return -1

    def get_adj(self, n, leftChild, rightChild):
        adj = {i: [] for i in range(n)}

        for i in range(n):
            if leftChild[i] != -1:
                adj[i].append(leftChild[i])
            if rightChild[i] != -1:
                adj[i].append(rightChild[i])
        return adj

    def dfs(self, adj, node, visited):
        if node in visited:
            return False
        if adj[node] == []:
            visited.add(node)
            return True

        visited.add(node)
        for nei in adj[node]:
            if not self.dfs(adj, nei, visited):
                return False
        return True
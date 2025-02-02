class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        suspicious = [0] * n

        for src, target in invocations:
            adj[src].append(target)
        print(adj)

        def check_suspicious(node):
            if suspicious[node] == 1:
                return
            suspicious[node] = 1
            for nei in adj[node]:
                check_suspicious(nei)
            return
        
        visited = set()
        def dfs(node):
            if suspicious[node]:
                return False
            if adj[node] == [] or node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei in visited:
                    continue
                if not dfs(nei):
                    return False
            return True

        # check all suspicious nodes
        check_suspicious(k)

        # can delete all suspicous nodes
        if sum(suspicious) == n:
            return []
        
        # check if any dependant on suspicious nodes
        res = []
        for i in range(n):
            if not suspicious[i]:
                if not dfs(i):
                    return [_ for _ in range(n)]
                res.append(i)
        return res

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, i):
        p = self.par[i]

        while p != self.par[p]:
            p = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)

        if par_a == par_b:
            return False
        if self.rank[par_a] >= self.rank[par_b]:
            self.par[par_b] = par_a
            self.rank[par_a] += self.rank[par_b]
        else:
            self.par[par_a] = par_b
            self.rank[par_b] += self.rank[par_a]
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        union_f = UnionFind(len(edges))
        indegree = [0] * (len(edges) + 1)

        for a, b in edges:
            indegree[b] += 1

        updated_edges = []
        invalid_edges = []
        for a, b in edges:
            if indegree[b] > 1:
                invalid_edges.append([a, b])
            else:
                updated_edges.append([a, b])
        updated_edges += invalid_edges

        res = [-1, -1]

        for a, b in updated_edges:
            if not union_f.union(a, b):
                res = [a, b]
            
        return res

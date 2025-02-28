class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)
    
    def find(self, x):
        p = self.par[x]

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
            self.rank[par_a] += self.rank[par_b]
            self.par[par_b] = par_a
        else:
            self.rank[par_b] += self.rank[par_a]
            self.par[par_a] = par_b
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for a, b in edges:
            if not union_find.union(a, b):
                return [a, b]

# Time: O(E*V). O(E) to union all edges. O(V) to find parent of the node
# Space: O(V + V)
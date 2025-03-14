class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.edges = 0
    
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
            self.rank[par_a] += self.rank[par_b]
            self.par[par_b] = par_a
        else:
            self.rank[par_b] += self.rank[par_a]
            self.par[par_a] = par_b
        self.edges += 1
        return True

    def get_edges(self):
        return self.edges


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        union_f = UnionFind(n)
        logs.sort(key=lambda x:x[0])

        for timestamp, a, b in logs:
            union_f.union(a, b)
            if union_f.get_edges() == n - 1:
                return timestamp
        return -1

# Time: O(nlogn)
# Space: O(n)
class UnionFind:
    def __init__(self, n):
        self.par = [_ for _ in range(n)]
        self.rank = [1] * n

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

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_f = UnionFind(26)

        for equation in equations:
            first = ord(equation[0]) - ord("a")
            second = ord(equation[3]) - ord("a")
            if equation[1] == "=":
                union_f.union(first, second)
        
        for equation in equations:
            first = ord(equation[0]) - ord("a")
            second = ord(equation[3]) - ord("a")
            if equation[1] == "!":
                par_first = union_f.find(first)
                par_second = union_f.find(second)
                if par_first == par_second:
                    return False
        return True

# Time: O(n)
# Space: O(26) = O(1)
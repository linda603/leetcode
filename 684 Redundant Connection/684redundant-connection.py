class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            p = par[x]

            while p != par[p]:
                p = par[par[p]]
                p = par[p]
            return p
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            if rank[pa] >= rank[pb]:
                rank[pa] += rank[pb]
                par[pb] = pa
            else:
                rank[pb] += rank[pa]
                par[pa] = pb
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]

# Time: O(E*V). E = V in this problem. Normally E = V - 1.
#.      Traverse all edges to union O(E)
#       Union takes O(V)
# Space: O(V)
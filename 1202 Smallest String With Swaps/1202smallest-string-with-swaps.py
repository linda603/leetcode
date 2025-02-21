class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        par = [i for i in range(len(s))]
        rank = [1] * len(s)
        
        def find(i):
            p = par[i]

            while p != par[p]:
                p = par[par[p]] 
                p = par[p]
            return p
        
        def union(a, b):
            par_a = find(a)
            par_b = find(b)

            if par_a == par_b:
                return False
            if rank[par_a] >= rank[par_b]:
                par[par_b] = par_a
                rank[par_a] += rank[par_b]
            else:
                par[par_a] = par_b
                rank[par_b] += rank[par_a]
            return True
        
        for i, j in pairs:
            # 1. Union-Find
            union(i, j)

        # 2. Grouping all idxes, chars with the same par
        group = {}
        for i, c in enumerate(s):
            par_i = find(i)
            if par_i not in group:
                group[par_i] = [[], []] # list 0: idx, list 1:char
            group[par_i][0].append(i)
            group[par_i][1].append(c)
        
        # 3. Sort idxes and chars for every group and form res
        res = [""] * len(s)
        for idxes, chars in group.values():
            idxes.sort()
            chars.sort()
            for i, c in zip(idxes, chars):
                res[i] = c
        return "".join(res)

# Time: O(nlogn)
# Space: O(n)
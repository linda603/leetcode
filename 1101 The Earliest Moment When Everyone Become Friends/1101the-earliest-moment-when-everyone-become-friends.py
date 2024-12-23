class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x:x[0])
        par = [i for i in range(n)]
        edges = 0

        def find(x):
            p = par[x]

            while p != par[p]:
                p = par[par[p]]
                p = par[p]
            return p

        def union(a, b):
            nonlocal edges
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return
            par[pb] = pa
            edges += 1
            return

        for timestamp, a, b in logs:
            union(a, b)
            if edges == n - 1:
                return timestamp
        return -1

# Time: O(mlogm + n + mn). m: len(logs)
# Space: O(m + n)
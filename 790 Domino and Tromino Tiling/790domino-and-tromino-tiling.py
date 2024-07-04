class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = {}

        def dfs(i, t1, t2):
            if i == n:
                return 1
            if (i, t1, t2) in dp:
                return dp[(i, t1, t2)]
            t3 = True if i + 1 < n else False
            t4 = t3
            
            count = 0
            if t1 and t2 and t3:
                count += dfs(i + 1, False, True)
            if t1 and t2 and t4:
                count += dfs(i + 1, True, False)
            if t1 and not t2 and t3 and t4:
                count += dfs(i + 1, False, False)
            if not t1 and t2 and t3 and t4:
                count += dfs(i + 1, False, False)
            if t1 and t2:
                count += dfs(i + 1, True, True)
            if t1 and t2 and t3 and t4:
                count += dfs(i + 1, False, False)
            if t1 and not t2 and t3:
                count += dfs(i + 1, False, True)
            if not t1 and t2 and t4:
                count += dfs(i + 1, True, False)
            if not t1 and not t2:
                count += dfs(i + 1, True, True)
            dp[(i, t1, t2)] = count % MOD
            return dp[(i, t1, t2)]
        
        return dfs(0, True, True)
                

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, curr):
            nonlocal res
            if i >= len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.is_pal(s, i, j):
                    curr.append(s[i: j + 1])
                    dfs(j + 1, curr)
                    curr.pop()
            return
        dfs(0, [])
        return res
    
    def is_pal(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Time: O(2^n*n). There are 2^n possible substrings. Each substring, takes O(n) for curr.copy() + O(n) for is_pal()
# Space: O(n + n)


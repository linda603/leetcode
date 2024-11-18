class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        count_s = {}
        count_p = {}

        for i in range(len(p)):
            count_p[p[i]] = 1 + count_p.get(p[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
        
        res = []
        if count_s == count_p:
            res.append(0)
        
        l = 0
        for r in range(len(p), len(s)):
            count_s[s[r]] = 1 + count_s.get(s[r], 0)
            count_s[s[l]] -= 1
            if count_s[s[l]] == 0:
                del count_s[s[l]]
            l += 1
            if count_s == count_p:
                res.append(l)

        return res

# Time: O(len(s))
# Space: O(1)
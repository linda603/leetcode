class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if ((s[i] in s_to_t and s_to_t[s[i]] != t[i]) 
                or (t[i] in t_to_s and t_to_s[t[i]] != s[i])):
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        return True

# Time: O(n)
# Space: O(2*26) = O(1)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        p_to_s = {}
        s_to_p = {}

        for i in range(len(pattern)):
            if ((pattern[i] in p_to_s and p_to_s[pattern[i]] != s[i]) or 
                (s[i] in s_to_p and s_to_p[s[i]] != pattern[i])):
                return False
            p_to_s[pattern[i]] = s[i]
            s_to_p[s[i]] = pattern[i]
        return True

# Time: O(m + n), m: len(pattern), n: len(s)
# Space: O(26 + n), n: len(s)
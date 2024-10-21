class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if abs(m - n) > 1: return False # more than 1 edit distance apart

        i, j = 0, 0
        while i < m and j < n and s[i] == t[j]:
            i += 1
            j += 1
        
        if i == m and j == n: return False # s equal to t, cannot edit 1 distance -> impossible

        if m == n: # len(s) == len(t), only replace is possible
            return s[i + 1:] == t[j + 1:]
        elif (m > n): # len(s) > len(t), only deletion is possible
            return s[i + 1:] == t[j:]
        else: # len(s) < len(t), only insertion is possible
            return s[i:] == t[j + 1:]

# Time: O(max(m, n))
# Space: O(max(m, n)) because we create substring s[i + 1:] == t[j + 1:]
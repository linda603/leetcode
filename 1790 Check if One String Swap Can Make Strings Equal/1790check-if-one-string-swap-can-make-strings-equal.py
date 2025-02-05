class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        s1_set = set()
        s2_set = set()
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
                if cnt > 2:
                    return False
                s1_set.add(s1[i])
                s2_set.add(s2[i])
        if (cnt == 0 or cnt == 2) and s1_set == s2_set:
            return True
        return False

# Time: O(n)
# Space: O(1). max size of s1_set: O(2)
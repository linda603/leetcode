class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = {}
        count2 = {}

        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        if count1 == count2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            
            if count1 == count2:
                return True
        return False

# Time: O(n). n: len(s2)
# Space: O(2 * 26) = O(1)

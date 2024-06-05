class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        #Binary search
        l = 0
        r = len(removable) - 1
        res = 0

        while l <= r:
            mid = (l + r) // 2
            needToRemove = set(removable[:mid + 1]) #To reduce time complexity
            if self.isValidSubSeq(s, p, needToRemove):
                res = max(res, mid + 1) #mid is the index, mid + 1 returns the number k
                l = mid + 1
            else:
                r = mid - 1
        return res


    def isValidSubSeq(self, s, p, needToRemove) -> bool:
        idxS = 0
        idxP = 0

        while idxS < len(s) and idxP < len(p):
            if idxS in needToRemove:
                idxS += 1
                continue
            if s[idxS] == p[idxP]:
                idxP += 1
            idxS += 1
        return True if idxP == len(p) else False

#Time: O(len(s) * logk), k is len of removable
#Space: O(1)
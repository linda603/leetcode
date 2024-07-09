class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = {}
        res = 0

        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        
        for num in seen:
            if k > 0 and num + k in seen:
                print(num, num + k)
                res += 1
            elif k == 0 and seen[num] > 1:
                res += 1
        
        return res

#Time: O(2n)
#Space: O(n)
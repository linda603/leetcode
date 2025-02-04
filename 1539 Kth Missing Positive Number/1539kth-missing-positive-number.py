class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums_set = set(arr)
        cnt = 0
        num = 1

        while cnt < k:
            if num not in nums_set:
                cnt += 1
            num += 1
        
        return num - 1

# Time: O(num)
# Space: O(n)
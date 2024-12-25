class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        events = [0] * (len(nums) + 1)
        
        for start, end in queries:
            events[start] += 1
            events[end + 1] -= 1
        
        count = 0
        for i, num in enumerate(nums):
            count += events[i]
            if count < num:
                print("i, num, count:", i, num, count)
                return False
        return True

# Time: O(q + n)
# Space: O(n)
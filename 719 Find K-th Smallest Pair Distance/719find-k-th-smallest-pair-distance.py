class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_pairs(diff):
            count = 0
            
            l = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > diff:
                    l += 1
                count += r - l
            return count

        l = 0
        r = max(nums)

        while l < r:
            mid = (l + r) // 2
            pairs = count_pairs(mid)
            if pairs < k:
                l = mid + 1
            else:
                r = mid # mid is possible diff at pair k - 1
        return r

#Time: O(nlogm). n: len(nums). m: max(nums). O(nlogm) < O(n^2)
#Space: O(n)
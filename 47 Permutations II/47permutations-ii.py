class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in count:
                if count[num]:
                    count[num] -= 1
                    dfs(curr + [num])
                    count[num] += 1
        dfs([])
        return res

#Time: O(n!*n)
#Space: O(n)
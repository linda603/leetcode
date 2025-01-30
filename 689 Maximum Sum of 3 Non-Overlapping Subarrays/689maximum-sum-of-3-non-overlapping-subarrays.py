class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # prefix_sum
        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])
        
        # get max sum
        cache = {}
        def dfs(i, cnt):
            if cnt >= 3 or i > len(nums) - k:
                return 0
            if (i, cnt) in cache:
                return cache[(i, cnt)]
            
            # include i
            include_i = k_sums[i] + dfs(i + k, cnt + 1)

            # skip i
            skip_i = dfs(i + 1, cnt)
            cache[(i, cnt)] = max(include_i, skip_i)
            return cache[(i, cnt)]
    
        def get_max_sum_path():
            i = 0
            res = []

            while i <= len(nums) - k and len(res) < 3:
                include = k_sums[i] + dfs(i + k, len(res) + 1)
                skip = dfs(i + 1, len(res))
            
                if include >= skip:
                    res.append(i)
                    i += k
                else:
                    i += 1
            return res

        dfs(0, 0)
        return get_max_sum_path()

# Time: O(3n + n)
# Space: O(3n)
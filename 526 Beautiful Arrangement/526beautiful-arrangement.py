class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        res = []

        def dfs(pos, curr):
            if pos == n and len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if (nums[i] % (pos + 1) == 0 or (pos + 1) % nums[i] == 0) and nums[i] not in curr:
                    curr.append(nums[i])
                    dfs(pos + 1, curr)
                    curr.pop()

            return
        dfs(0, [])
        return len(res)

#Time: O(k) k is the number of valid permutations
#Space: O(n) size of nums is n


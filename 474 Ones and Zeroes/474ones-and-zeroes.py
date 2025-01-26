class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # DP
        DP = defaultdict(int)

        for i in range(len(strs) - 1, -1, -1):
            zero_cnt = self.get_zero(strs[i])
            one_cnt = self.get_one(strs[i])
            for zero in range(m + 1):
                for one in range(n + 1):
                    DP[(i, zero, one)] = DP[(i + 1, zero, one)]
                    if zero - zero_cnt >= 0 and one - one_cnt >= 0:
                        DP[(i, zero, one)] = max(DP[(i, zero, one)], 
                                        1 + DP[(i + 1, zero - zero_cnt, one - one_cnt)])
        return DP[(0, m, n)]

    def get_one(self, string):
        res = 0

        for c in string:
            res += 1 if c == "1" else 0
        return res
    
    def get_zero(self, string):
        res = 0

        for c in string:
            res += 1 if c == "0" else 0
        return res

# Time: O(smn). s: len(strs)
# Space: O(smn)
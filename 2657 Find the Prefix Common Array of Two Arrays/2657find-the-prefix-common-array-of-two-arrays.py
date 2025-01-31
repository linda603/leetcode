class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        idx_a_map = {}
        res = [0] * len(A)

        for i, num in enumerate(A):
            idx_a_map[num] = i
        
        for i, num in enumerate(B):
            res[i] += res[i - 1] if i - 1 >= 0 else 0
            if idx_a_map[num] > i:
                res[idx_a_map[num]] = 1
            else:
                res[i] += 1
        return res

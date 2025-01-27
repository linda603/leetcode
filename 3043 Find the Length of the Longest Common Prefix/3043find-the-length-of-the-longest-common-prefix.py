class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        prefix = set()

        for num in arr1:
            while num:
                if num not in prefix:
                    prefix.add(num)
                num = num // 10
        
        for num in arr2:
            while num:
                if num in prefix:
                    res = max(res, len(str(num)))
                    break
                num = num // 10
        return res

# Time: O(n1*log10(num) + n2*log10(num))
# Space: O(n1*log10(num))
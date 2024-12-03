class Solution:
    def nearestPalindromic(self, n: str) -> str:
        all_pos = []
        
        if len(n) % 2:
            is_odd = True
            mid = len(n) // 2
        else:
            is_odd = False
            mid = len(n) // 2 - 1
        half = int(n[: mid + 1])

        all_pos.append(self.half_to_pal(half, is_odd))
        all_pos.append(self.half_to_pal(half - 1, is_odd))
        all_pos.append(self.half_to_pal(half + 1, is_odd))
        all_pos.append(10 ** (len(n) - 1) - 1)
        all_pos.append(10 ** len(n) + 1)
    
        print(all_pos)
        res = float("inf")
        min_diff = float("inf")
        for num in all_pos:
            if num == int(n):
                continue
            curr = abs(num - int(n))
            if curr < min_diff:
                min_diff = curr
                res = num
            elif curr == min_diff:
                res = min(res, num)
        return str(res)
    
    def half_to_pal(self, half, is_odd):
        res = half

        if is_odd:
            half = half // 10
        
        while half > 0:
            res = res * 10 + half % 10
            half = half // 10
        return res

# Time: O(5*n/2) = O(n)
# Space: O(n) due to building first half = n[: mid + 1]
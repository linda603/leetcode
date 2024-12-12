class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        while k:
            max_idx = 0
            for i, g in enumerate(gifts):
                if g > gifts[max_idx]:
                    max_idx = i
            gifts[max_idx] = int(sqrt(gifts[max_idx]))
            k -= 1
        return sum(gifts)

# Time: O(nk)
# Space: O(1)
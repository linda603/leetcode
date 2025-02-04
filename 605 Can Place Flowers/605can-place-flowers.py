class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        
        # Find all number of flowers can planted
        for i in range(len(flowerbed)):
            if not flowerbed[i] and ((i - 1 < 0 or not flowerbed[i - 1]) and (i + 1 == len(flowerbed) or not flowerbed[i + 1])):
                cnt += 1
                flowerbed[i] = 1
        return n <= cnt

# Time: O(n)
# Space: O(1)
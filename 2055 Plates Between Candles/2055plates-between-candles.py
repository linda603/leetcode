class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_idx = []
        
        for i, c in enumerate(s):
            if c == '|':
                candle_idx.append(i)
        
        res = []
        for start, end in queries:
            if end - start > 1:
                left_most_candle = self.binary_search(candle_idx, start, True) # find lower bound, will return same index if same with start else first greater
                right_most_candle = self.binary_search(candle_idx, end, False) # find upper bound, will return same index if same with end else first smaller

                if left_most_candle >= right_most_candle:
                    res.append(0)
                    continue
                else:
                    # range between right and left most candles - (right_most_candle - left_most_candle - 1): number of candles in between
                    count = candle_idx[right_most_candle] - candle_idx[left_most_candle] - 1 - (right_most_candle - left_most_candle - 1)
                    res.append(count)
            else:
                res.append(0)
        return res

    def binary_search(self, nums, target, is_left):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if is_left: # return first greater
            return l
        else: # return first smaller
            return r

# Time: O(n + q*2logn). n: len(s), q: len(queries)
# Space: O(n + q) for candle_idx array, q for res array
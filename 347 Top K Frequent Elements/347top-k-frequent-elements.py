class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # count all freq of num
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # add all num with same freq into freq, ignore 0 freq
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            lists = freq[i]
            while lists and k:
                res.append(lists.pop())
                k -= 1
        return res

# Time: O(n + n + n + k) = O(n)
# Space: O(n + k)
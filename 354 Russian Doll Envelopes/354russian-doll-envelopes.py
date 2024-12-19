class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort increasing for w, decreasing for h
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        seq = []

        # LIS of h
        for w, h in envelopes:
            if not seq or seq[-1] < h:
                seq.append(h)
            else:
                replace_i = self.upper_bound(seq, h)
                seq[replace_i] = h
        return len(seq)
    
    def upper_bound(self, seq, target):
        l = 0
        r = len(seq) - 1
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if seq[mid] == target:
                return mid
            if seq[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Time: O(nlogn + nlogn)
# Space: O(n + n)
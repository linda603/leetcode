class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (len(citations) + 1)

        for val in citations:
            count[min(val, n)] += 1
        
        h = n
        num_papers = count[h]

        while h > num_papers:
            h -= 1
            num_papers += count[h]
        return h

# Time: O(2n)
# Space: O(n)
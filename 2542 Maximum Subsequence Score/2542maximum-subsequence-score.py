class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort pair (nums1[i], nums2[i]) by nums2[i] in decreasing order
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse = True)
        print(pairs)

        # Use min Heap to maintain top k elements from nums1
        minHeap = []
        n1Sum = 0
        res = 0

        # n2 is always the smallest number among k elemnents
        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1) # Add curr nums1 to heap
            if len(minHeap) > k: # Remove the smallest num from nums1 in heap
                n1pop = heapq.heappop(minHeap)
                n1Sum -= n1pop 
            if len(minHeap) == k:
                res = max(res, n1Sum * n2) # Update answer as maximum score for k pairs
        return res

#Time: O(nlogn)
#Space: O(n)
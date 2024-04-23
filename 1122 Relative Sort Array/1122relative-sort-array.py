class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqs = {}
        output1 = []
        output2 = []
        
        for num in arr1:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
        
        for num in arr2:
            output1 += [num] * freqs[num]
        
        for num in (set(arr1) - set(arr2)):
            output2 += [num] * freqs[num]
        
        return output1 + sorted(output2)        
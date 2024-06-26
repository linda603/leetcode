class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        #Iterate through freqs hash map and insert the frequencies to the set
        #if size of the freqs map is not equal to set's size, meaning the frequencies are not unique
        if len(freq) != len(set(freq.values())):
            return False
        
        return True

#Time: O(n)
#Space: O(n)
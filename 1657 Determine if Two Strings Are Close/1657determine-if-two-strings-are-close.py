class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in word1:
            freq1[ord(char) - ord('a')] += 1
        
        for char in word2:
            freq2[ord(char) - ord('a')] += 1
        
        #To check if char in present in word1 and not in word2 or the opposite. Return False 
        for i in range(len(freq1)):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        if freq1 != freq2:
            return False

        return True
        
#Time: O(n)
#Space: O(1)
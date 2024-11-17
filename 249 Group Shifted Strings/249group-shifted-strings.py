class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # dist (): [string]

        for string in strings:
            if len(string) == 1:
                groups[(-1)].append(string)
            else:
                diff = []
                for i in range(1, len(string)):
                    diff.append((ord(string[i]) - ord(string[i - 1]) + 26) % 26)
    
                groups[tuple(diff)].append(string)
        
        return list(groups.values())

# Time: O(nl). n: len(string), l: len(longest string)
# Space: O(nl)
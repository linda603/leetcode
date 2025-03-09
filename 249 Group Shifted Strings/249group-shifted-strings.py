class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for word in strings:
            if len(word) == 1:
                if () not in groups:
                    groups[()] = []
                groups[()].append(word)
            else:
                diff = []
                for i in range(1, len(word)):
                    diff.append((ord(word[i]) - ord(word[i - 1]) + 26) % 26)
                if tuple(diff) not in groups:
                    groups[tuple(diff)] = []
                groups[tuple(diff)].append(word)
        return list(groups.values())

# Time: O(nl)
# Space: O(nl)
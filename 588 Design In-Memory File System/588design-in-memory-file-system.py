class trie_node:
    def __init__(self):
        self.children = {}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = trie_node()

    def ls(self, path: str) -> List[str]:
        dirs = path.split("/")
        curr = self.root

        for d in dirs:
            if not d: continue
            curr = curr.children[d]
        if curr.content: # this is a file path
            return [d]
        res = [d for d in curr.children.keys()]
        res.sort()
        return res

    def mkdir(self, path: str) -> None:
        dirs = path.split("/") # /a/b/c -> ["", "a", "b", "c"]
        curr = self.root

        for d in dirs:
            if not d: continue
            if d not in curr.children:
                curr.children[d] = trie_node()
            curr = curr.children[d]

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split("/")
        curr = self.root

        for d in dirs:
            if not d: continue
            if d not in curr.children:
                curr.children[d] = trie_node()
            curr = curr.children[d]
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split("/")
        curr = self.root

        for d in dirs:
            if not d: continue
            curr = curr.children[d]
        return curr.content

# Time: ls(). O(n + m + klogk). n: len(path), m: len(dirs), k: len(res)
#.      mkdir(): O(n + m)
#.      addContentToFile(): O(n + m)
#       readContentToFile(): O(n + m)
# Space: O(m), len of trie

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []

        self.dfs(nestedList)
        self.arr.reverse()
    
    def next(self) -> int:
        return self.arr.pop()
    
    def hasNext(self) -> bool:
        return self.arr
    
    def dfs(self, nestedList):
        for sub_item in nestedList:
            if sub_item.isInteger():
                self.arr.append(sub_item.getInteger())
            else:
                self.dfs(sub_item.getList())
        return

# Time: constructor(): O(n). next(): O(1), hasNext(): O(1)
# Space: O(n)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
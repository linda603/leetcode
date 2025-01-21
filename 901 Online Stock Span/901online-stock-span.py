class StockSpanner:

    def __init__(self):
        self.stack = [] # decreasing monotonic stack (price, span)

    def next(self, price: int) -> int:
        cnt = 1
        # pop lower price from the stack and accumulate the cnt
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1]
        self.stack.append((price, cnt))
        return cnt

# Time: O(n)
# Space: O(n)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
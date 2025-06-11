class StockSpanner:

    def __init__(self):
        
        self.mon_stock = []
    def next(self, price: int) -> int:
        span = 1
        while self.mon_stock and price >= self.mon_stock[-1][0]:
            span += self.mon_stock.pop()[1]
        self.mon_stock.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
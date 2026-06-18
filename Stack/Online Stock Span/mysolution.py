class StockSpanner:

    def __init__(self):
        self.stk=[]

    def next(self, price: int) -> int:
        count=1
        while self.stk and self.stk[-1][0]<=price:
            stk_p,stk_i=self.stk.pop()
            count+=stk_i
        self.stk.append((price,count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

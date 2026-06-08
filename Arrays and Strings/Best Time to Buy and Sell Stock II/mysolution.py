class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        last=float("inf")
        for i in prices:
            if i>last:
                profit+=i-last
            last=i
        return profit

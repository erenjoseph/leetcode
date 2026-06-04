class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap=float('inf')
        profit=0
        for num in prices:
            if num<cheap:
                cheap=num
            p=num-cheap
            if p>profit:
                profit=p
        return profit
            

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high=max(weights),sum(weights)
        while low<high:
            mid=(low+high)//2
            ship=1
            cap=0
            for i in weights:
                if cap+i>mid:
                    ship+=1
                    cap=i
                else:
                    cap+=i
            
            if ship>days:
                low=mid+1
            else:
                high=mid
        
        return high

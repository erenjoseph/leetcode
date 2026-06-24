class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weight):
            curr_weight=0
            no_of_days=0
            for i in weights:
                curr_weight+=i
                if curr_weight>weight:
                    no_of_days+=1
                    curr_weight=i
            if curr_weight>0:
                no_of_days+=1
            return no_of_days<=days

        low=high=0
        for i in weights:
            low=max(low,i)
            high+=i
        while low<high:
            mid=low+(high-low)//2
            if check(mid):
                high=mid
            else:
                low=mid+1
        return low

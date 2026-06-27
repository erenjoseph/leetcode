class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=0
        high=sum(nums)
        def perfect(target):
            count=1
            curr=0
            for i in nums:
                if i>target:
                    return False
                curr+=i
                if curr>target:
                    count+=1
                    curr=i
                
            return count<=k
            
        while low<high:
            mid=(low+high)//2
            if perfect(mid):
                high=mid
            else:
                low=mid+1
        return high

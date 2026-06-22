class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        for _ in range(n):
            mid=(low+high)//2
            if nums[mid]<target:
                low+=1
            elif nums[mid]>target:
                high-=1
            else:
                return mid
        
        return -1

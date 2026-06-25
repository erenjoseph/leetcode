class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        mini=high
        if mini==0:
            low,high=0,n-1
        elif target>=nums[0] and target<=nums[mini-1]:
            low,high=0,mini-1
        else:
            low,high=mini,n-1
        
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                return mid
        
        return -1


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        low=1
        high=n-2
        #Search for the peak
        while low<=high:
            mid=(low+high)//2
            left,m,right=mountainArr.get(mid-1),mountainArr.get(mid),mountainArr.get(mid+1)
            if left<m<right:
                low=mid+1
            elif left>m>right:
                high=mid-1
            else:
                break
        
        peak=mid

        #search the left portion
        low,high=0,peak
        while low<=high:
            mid=(low+high)//2
            val=mountainArr.get(mid)
            if val<target:
                low=mid+1
            elif val>target:
                high=mid-1
            else:
                return mid

        #search the right portion
        low,high=peak,n-1
        while low<=high:
            mid=(low+high)//2
            val=mountainArr.get(mid)
            if val<target:
                high=mid-1
            elif val>target:
                low=mid+1
            else:
                return mid
        
        return -1

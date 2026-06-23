class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nest=[]
        for i in matrix:
            nest.extend(i)
        low=0
        high=len(nest)-1
        while low<=high:
            mid=(low+high)//2
            if nest[mid]<target:
                low=mid+1
            elif nest[mid]>target:
                high=mid-1
            else:
                return True
        
        return False

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        if n>m:
            return self.findMedianSortedArrays(nums2,nums1)
        n=len(nums1)
        m=len(nums2)
        low=0
        high=n
        while low<=high:
            mid1=(low+high)//2
            mid2=(n+m+1)//2-mid1 # The +1 trick forces the extra element to the left side if the total length is odd.
            maxleft1=float('-inf') if mid1==0 else nums1[mid1-1]
            minright1=float('inf') if mid1==n else nums1[mid1]
            maxleft2=float('-inf') if mid2==0 else nums2[mid2-1]
            minright2=float('inf') if mid2==m else nums2[mid2]

            if maxleft1<=minright2 and maxleft2<=minright1:
                if (n+m)%2==0:
                    return ((max(maxleft1,maxleft2)+min(minright1,minright2))/2)
                else:
                    return (max(maxleft1,maxleft2))
            elif maxleft1>minright2:
                high=mid1-1
            else:
                low=mid1+1

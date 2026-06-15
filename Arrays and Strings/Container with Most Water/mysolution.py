class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_area=0
        while i<j:
            w=j-i
            h=min(height[i],height[j])
            a=w*h
            max_area=max(max_area,a)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return max_area

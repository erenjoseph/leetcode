class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        s=set()
        i=0
        while i<len(nums)-2:
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[left]+nums[right]+nums[i]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    s.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
            i+=1
        return list(s)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out=set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                h=len(nums)-1

                while l<h:
                    #print(nums[i],nums[j],nums[l],nums[h])
                    if nums[i]+nums[j]+nums[l]+nums[h]==target:
                        out.add([nums[i],nums[j],nums[l],nums[h]])
                        
                    if nums[i]+nums[j]+nums[l]+nums[h]>target:
                        h-=1
                    else:
                        l+=1
        return out

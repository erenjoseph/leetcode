class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        clos=nums[0]
        for i in range(len(nums)):
            if abs(nums[i])<=abs(clos):
                if abs(nums[i])==abs(clos):
                    clos=max(clos,nums[i])
                else:
                    clos=nums[i]
        return clos

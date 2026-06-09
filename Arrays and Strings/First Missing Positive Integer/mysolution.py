class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=[i for i in nums if i>0]
        target=1
        nums.sort()
        for i in nums:
            if i==target:
                target+=1
            elif i>target:
                return target
        return target

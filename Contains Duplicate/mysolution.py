class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        a=len(nums)
        if a==1:
            return False


        for i in range(a-1):
            if nums[i]==nums[i+1]:
                return True
        return False

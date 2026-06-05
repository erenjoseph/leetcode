class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return count

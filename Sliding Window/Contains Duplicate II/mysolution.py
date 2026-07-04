class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        s={}
        for i in range(n):
            if nums[i] in s:
                if abs(s[nums[i]]-i)<=k:
                    return True
            
            s[nums[i]]=i
        
        return False

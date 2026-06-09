class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq1, freq2 = 0, 0
        ans1, ans2 = 0, 0
        
        for i in range(n):
            if ans1 == nums[i]:
                freq1 += 1
            elif ans2 == nums[i]:
                freq2 += 1    
            elif freq1 == 0:
                ans1 = nums[i]
                freq1 = 1  
            elif freq2 == 0:
                ans2 = nums[i]
                freq2 = 1  
            else:
                freq1 -= 1
                freq2 -= 1
        temp = []
        m = n // 3
        if nums.count(ans1) > m:
            temp.append(ans1)
        if ans2 != ans1 and nums.count(ans2) > m:
            temp.append(ans2) 
        return temp

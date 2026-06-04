class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = 0
        res = []
        while r <= len(nums) - 1:
            if r == len(nums) - 1 or nums[r + 1] != nums[r] + 1:
                if (r - l >= 1):
                    res.append(f'{nums[l]}->{nums[r]}')
                else:
                    res.append(f'{nums[l]}')
                r += 1
                l = r
            else:
                r += 1
        return res

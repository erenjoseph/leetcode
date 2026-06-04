class Solution:
    def twoSum(self, nums: List[int], target: int):
        dic = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in dic:
                return [dic[want], i]
            dic[nums[i]] = i
        return []

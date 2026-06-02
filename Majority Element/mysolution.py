class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)
        for num,count in count.most_common():
            if count>n/2:
                return num

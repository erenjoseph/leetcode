class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter=collections.Counter()
        current=0
        counter[0]=1
        rollingsum=0
        total=0
        for num in nums:
            rollingsum+=num
            x=rollingsum-k
            total+=counter[x]
            counter[rollingsum]+=1
        return total

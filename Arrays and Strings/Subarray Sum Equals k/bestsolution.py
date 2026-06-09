class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = dict()
        seen[0] = 1
        p = 0
        cnt = 0
        for n in nums:
            p += n
            need = p-k
            cnt += seen.get(need, 0)
            seen[p] = seen.get(p, 0) + 1
        return cnt

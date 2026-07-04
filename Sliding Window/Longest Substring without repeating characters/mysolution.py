class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=set()
        l=0
        longest=0
        n=len(s)
        for r in range(n):
            while s[r] in k:
                k.remove(s[l])
                l+=1
            w=(r-l)+1
            k.add(s[r])
            longest=max(longest,w)
        
        return longest

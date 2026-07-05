class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        n=len(s)
        counts=[0]*26
        l=0
        for r in range(n):
            counts[ord(s[r])-ord('A')]+=1
            w=(r-l)+1
            m=max(counts)
            while (w-m)>k:
                counts[ord(s[l])-ord('A')]-=1
                l+=1
                w=(r-l)+1
            longest=max(longest,w)
        
        return longest

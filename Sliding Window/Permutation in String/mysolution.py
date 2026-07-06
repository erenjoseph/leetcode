class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1=[0]*26
        counts2=[0]*26
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        for i in range(n):
            counts1[ord(s1[i])-ord('a')]+=1
            counts2[ord(s2[i])-ord('a')]+=1
        
        if counts1==counts2:
            return True
        for i in range(n,m):
            counts2[ord(s2[i])-ord('a')]+=1
            counts2[ord(s2[i-n])-ord('a')]-=1
            if counts1==counts2:
                return True
        return False

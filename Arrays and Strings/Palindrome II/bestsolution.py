class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        if s==s[::-1]:
            return True
        else:
            while left<right:
                if s[left]!=s[right]:
                    a=s[left+1:right+1]
                    b=s[left:right]
                    return a == a[::-1] or b == b[::-1]
                left=left+1
                right=right-1
        return True
        '''if s==s[::-1]:
            return True
        for i in range(len(s)):
            x=s[:i]+s[i+1:]
            if x==x[::-1]:
                return True
        return False'''        

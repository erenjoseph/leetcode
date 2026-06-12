class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A=len(word1)
        B=len(word2)
        a,b=0,0
        result=""
        while a<A and b<B:
            result+=word1[a]+word2[b]
            a+=1
            b+=1
        if a<A:
            result+=word1[a:]
        if b<B:
            result+=word2[b:]
        return result

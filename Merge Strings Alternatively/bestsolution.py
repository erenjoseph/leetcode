class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # we need a pointer for the first word
        counter = 0

        #store the result in a list
        res = []

        # loop till we've finished the first word
        while counter < len(word1) or counter < len(word2):

            # if we're at word1, append it
            if counter < len(word1):
                res.append(word1[counter])
            
            if counter < len(word2):
                res.append(word2[counter])
            
            counter += 1

        return ''.join(res)
            




        OR


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        n=min(n1,n2)
        res=""
        for i in range(n):
            res+=word1[i]+word2[i]
        if n1>n2:
            res+=word1[n:]
        else:
            res+=word2[n:]
        return res

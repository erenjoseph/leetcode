#this is to understand the problem well. This one avoids ghost duplication  but takes a lot of time. So better solution is "mysolution.py".
#this is one works too and passes all testcases in leetcode. Better option is the code mentioned in the above file.
#why it takes a lot of time even thought its O(n)? Because of including a list and appending it.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        i=0
        j=n-1
        res=[]
        boat=0
        while i<=j:
            if j==i:
                res.append(people[i])
                i+=1
                j-=1
            elif people[i]+people[j]<=limit:
                    res.append((people[i],people[j]))
                    i+=1
                    j-=1
            else:
                res.append((people[j]))
                j-=1
            boat+=1
        print(res)
        return boat
                

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        i=0
        j=n-1
        boat=0
        while i<=j:
            if people[i]+people[j]<=limit:
                    i+=1
                    j-=1
            else:
                j-=1
            boat+=1 #boat takes off no matter what happens. So it doesnt care abt ghost duplication in odd sized array
        return boat
                

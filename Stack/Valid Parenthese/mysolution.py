class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        st=[]
        for i in s:
            if i not in hashmap:
                st.append(i)
            else:
                if not st:
                    return False
                popped=st.pop()
                if popped!=hashmap[i]:
                    return False
        
        return not st

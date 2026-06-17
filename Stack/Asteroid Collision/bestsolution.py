class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for cur in asteroids:
            while st and st[-1]>0 and cur<0:
                top=st[-1]
                if abs(cur)>top:
                    st.pop()
                    continue
                elif abs(cur)==top:
                    st.pop()
                break
            else:
                st.append(cur)
        return st

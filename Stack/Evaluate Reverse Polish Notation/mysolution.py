class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans_stk=[]
        for i in tokens:
            if i=="/":
                ans=int(ans_stk[-2]/ans_stk[-1])
                ans_stk.pop()
                ans_stk.pop()
                ans_stk.append(ans)
            elif i=="+":
                ans=ans_stk[-2]+ans_stk[-1]
                ans_stk.pop()
                ans_stk.pop()
                ans_stk.append(ans)
            elif i=="-":
                ans=ans_stk[-2]-ans_stk[-1]
                ans_stk.pop()
                ans_stk.pop()
                ans_stk.append(ans)
            elif i=="*":
                ans=ans_stk[-2]*ans_stk[-1]
                ans_stk.pop()
                ans_stk.pop()
                ans_stk.append(ans)
            else:
                ans_stk.append(int(i))
        return ans_stk[-1]

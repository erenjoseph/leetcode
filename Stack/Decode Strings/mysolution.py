class Solution:
    def decodeString(self, s: str) -> str:
        num=0
        stk=[]
        count=[]
        res=''
        for i in s:
            if i.isdigit():
                num=num*10+(ord(i)-ord('0'))
            elif i=='[':
                stk.append(res)
                count.append(num)
                res=''
                num=0
            elif i==']':
                res=stk.pop()+count.pop()*res
            else:
                res+=i
        
        return res

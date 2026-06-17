class MinStack:

    def __init__(self):
        self.stk=[]
        self.min_st=[]

    def push(self, value: int) -> None:
        self.stk.append(value)

        if not self.min_st:
            self.min_st.append(value)
        elif self.min_st[-1] < value:
            self.min_st.append(self.min_st[-1])
        else:
            self.min_st.append(value)


    def pop(self) -> None:
        self.stk.pop()
        self.min_st.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while matrix:
                row=matrix.pop(0)
                ans.extend(row)
                matrix = list(zip(*matrix))[::-1]

        return ans
        

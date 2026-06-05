class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        i,j=0,0
        direction=0
        right,left,up,down=0,1,2,3
        UP_WALL=0
        RIGHT_WALL=m
        DOWN_WALL=n
        LEFT_WALL=-1
        ans=[]
        while len(ans)!=m*n:
            if direction==right:
                while j<RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                RIGHT_WALL-=1
                direction=down
            elif direction==down:
                while i<DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                DOWN_WALL-=1
                direction=left
            elif direction==left:
                while j>LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                direction=up
                LEFT_WALL+=1
                direction=up
            else:
                while i>UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                direction=right
                UP_WALL+=1
                direction=right
        return ans

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        transpose=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                transpose[j][i]=matrix[i][j]
        matrix[:]=transpose
        for i in range(len(matrix)):
            matrix[i].reverse()

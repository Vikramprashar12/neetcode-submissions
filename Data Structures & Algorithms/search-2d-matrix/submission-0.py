class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix[0]), len(matrix)
        l, r = 0, (row*col)-1
        print(l)
        print(r)
        while l<=r:
            m = ((l+r)//2)
            if matrix[m//row][m%row] < target:
                l=m+1
            elif matrix[m//row][m%row] > target:
                r = m - 1
            else:
                return True
        return False
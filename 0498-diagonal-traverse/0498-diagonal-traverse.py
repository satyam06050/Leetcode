class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []
        
        for d in range(rows + cols - 1):
            diagonal = []
            
            # Starting row and column for this diagonal
            r = max(0, d - cols + 1)
            c = min(d, cols - 1)
            
            while r < rows and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1
            
            # Even diagonal → reverse direction
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)
        
        return result
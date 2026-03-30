class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rowLen = len(matrix[0])

        left = 0
        right = (rowLen * len(matrix)) - 1

        while left <= right:
            middle = (left + right) // 2
            i = middle // rowLen
            j = middle % rowLen
            
            print("i: ", i, "j: ", j)

            
            if matrix[i][j] < target:
                left = middle + 1
            elif matrix[i][j] > target:
                right = middle - 1
            else:
                return True 
        return False
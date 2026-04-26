class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r_len = len(matrix)
        c_len = len(matrix[0])
        
        n = c_len * r_len
        
        left, right = 0, n - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            r = mid // c_len
            c = mid % c_len

            guess = matrix[r][c]

            if guess == target:
                return True
            elif guess > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
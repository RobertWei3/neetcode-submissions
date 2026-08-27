class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows ,cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r :
            mid = l + (r -l) // 2
            current_val = matrix[mid // cols][mid % cols]
            if current_val == target:
                return True
            elif current_val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
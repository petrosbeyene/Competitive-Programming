class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = low + (high - low)//2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                break

        low, high = 0, len(matrix[mid])-1
        pos_ls = matrix[mid]
        while low <= high:
            mid = low + (high-low)//2
            if pos_ls[mid] == target:
                return True
            elif pos_ls[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
        ## time complexity: O(log(m*n)) 
        ## space complexity: O(1)

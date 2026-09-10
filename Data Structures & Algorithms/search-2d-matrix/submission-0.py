class Solution:
    def find_left(self,matrix,target):
        res = -1
        l = 0
        r = len(matrix) -1

        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] > target:
                r = mid -1
            else:
                res = mid
                l = mid + 1

        return res
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.find_left(matrix,target)

        if idx == -1: 
            return False

        left = 0
        right = len(matrix[0])-1

        while left <= right:
            mid = (left+right)//2

            curr = matrix[idx][mid]

            if curr == target:
                return True
            elif curr > target:
                right -=1
            else:
                left += 1

        return False
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n < 3:
            return 0
        max_left = [0]*(n)
        max_right = [0]*(n)

        max_left[1] = height[0]

        for i in range(2,n):
            max_left[i] = max(max_left[i-1],height[i-1])

        max_right[n-2] = height[n-1]

        for j in range(n-3,-1,-1):
            max_right[j] = max(max_right[j+1],height[j+1])

        total_water = 0

        for i in range(1,n-1):
            m = min(max_right[i],max_left[i])

            if m > height[i]:
                total_water += (m-height[i])

        return total_water
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = deque()
        n = len(temperatures)
        res = [0]*n

        for i in range(n):

            while st and temperatures[st[-1]] < temperatures[i]:
                prev = st.pop()

                res[prev] = i-prev
            st.append(i)

        return res
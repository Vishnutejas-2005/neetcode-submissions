class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back_(curr,front,back,n):
            if front == back and front == n:
                res.append(curr)
                return

            if front < n:
                back_(curr+"(",front+1,back,n)
            if back < front:
                back_(curr+")",front,back+1,n)
                
        back_("",0,0,n)
        return res

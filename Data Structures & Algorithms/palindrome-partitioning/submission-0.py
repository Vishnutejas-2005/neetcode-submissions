class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        def back(curr,start):
            if start == n:
                res.append(curr)
                return

            for j in range(start,n):
                sub_string = s[start:j+1]
                if sub_string == sub_string[::-1]:
                    back(curr + [sub_string],j+1)
        back([],0)
        return res 

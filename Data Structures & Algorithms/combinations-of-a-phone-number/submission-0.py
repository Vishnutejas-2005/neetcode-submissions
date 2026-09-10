class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        n = len(digits)
        if n == 0:
            return []
        d = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        def back(i,curr):
            if i == n:
                res.append(curr)
                return

            for j in d[int(digits[i])]:
                back(i+1,curr+j)
        
        back(0,"")
        return res
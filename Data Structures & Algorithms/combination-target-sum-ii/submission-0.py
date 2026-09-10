class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def back(cl,cs,i,n):
            if cs == target:
                res.append(cl)
                return

            for j in range(i,n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if candidates[j] +cs > target:
                    break

                back(cl+[candidates[j]],cs+candidates[j],j+1,n)
        back([],0,0,len(candidates))
        return res

                
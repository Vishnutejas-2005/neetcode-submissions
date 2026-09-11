class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = target

        ma,mb,mc = 0,0,0

        for i,j,k in triplets:
            if i >a or j>b or k>c:
                continue

            if i>ma:
                ma = i
            if j>mb:
                mb = j
            if k > mc:
                mc = k

        return ma==a and mb ==b and mc ==c
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#" + s

        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        if s == "":
            return []
        i = 0
        while s[i] != "#":
            i += 1

        l = int(s[:i])

        return [s[i+1:i+1+l]] + self.decode(s[i+1+l:])
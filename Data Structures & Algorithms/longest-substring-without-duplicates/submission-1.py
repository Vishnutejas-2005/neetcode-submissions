class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        n = len(s)

        start = -1
        max_len = 0

        for i in range(n):
            if d.get(s[i],-1) == -1:
                max_len = max(max_len,i-start)
                d[s[i]] = i
            else:
                start = max(start,d[s[i]])
                max_len = max(max_len,i-start)
                d[s[i]] = i

        return max_len
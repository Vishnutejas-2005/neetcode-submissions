from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count =  Counter(t)
        curr = Counter()

        have = 0
        need_count = len(count)

        l = 0
        res = ""
        res_len = float("inf")

        for r in range(len(s)):
            ch = s[r]
            curr[ch] += 1

            if ch in count and count[ch] == curr[ch]:
                have += 1

            while have == need_count:
                if r-l + 1 < res_len:
                    res_len = r-l +1
                    res = s[l:r+1]

                left_ch = s[l]
                curr[left_ch] -= 1

                if left_ch in count and curr[left_ch] < count[left_ch]:
                    have -= 1

                l += 1
        return res

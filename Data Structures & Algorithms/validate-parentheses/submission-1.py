from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                elif i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "}" and st[-1] == "{":
                    st.pop()
                elif i == "]" and st[-1] == "[":
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False
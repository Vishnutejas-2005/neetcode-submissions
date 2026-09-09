from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for i in tokens:
            if i in "+-*/":
                b = st.pop()
                a = st.pop()
                if i  == "+":
                    st.append(a+b)
                elif i == "-":
                    st.append(a-b)
                elif i == "*":
                    st.append(a*b)
                else:
                    st.append(int(a/b))
                    
            else:
                st.append(int(i))

        return st[-1]
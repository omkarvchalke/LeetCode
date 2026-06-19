class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t in "+-*/":
                n2 = stk.pop()
                n1 = stk.pop()

                if t == "+":
                    stk.append(n1 + n2)
                elif t == "-":
                    stk.append(n1 - n2)
                elif t == "*":
                    stk.append(n1 * n2)
                elif t == "/":
                    # truncate toward zero
                    stk.append(int(n1 / n2))
            else:
                stk.append(int(t))

        return stk[0]
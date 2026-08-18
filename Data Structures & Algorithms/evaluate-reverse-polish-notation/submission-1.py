class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/" :
                second = stack.pop()
                first = stack.pop()
                if i == "+":
                    new = first + second
                    stack.append(new)
                    continue
                if i == "-":
                    new = first - second
                    stack.append(new)
                    continue
                if i == "*":
                    new = first * second
                    stack.append(new)
                    continue
                if i == "/":
                    new = int(first / second)
                    stack.append(new)
                    continue
            else:
                temp = int(i)
                stack.append(temp)

        ans = stack.pop()

        return ans

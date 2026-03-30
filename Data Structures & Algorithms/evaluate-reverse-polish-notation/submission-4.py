class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operants = set({"+", "-", "*", "/"})

        output = "Null"

        stack = []

        for i in range(0, len(tokens)):
            if tokens[i] not in operants:
                stack.append(int(tokens[i]))
            else:
                curr = int(stack.pop())
                prev = int(stack.pop())

                if tokens[i] == "+":
                    stack.append(int(prev + curr))
                if tokens[i] == "-":
                    stack.append(int(prev - curr))
                if tokens[i] == "/":
                    stack.append(int(prev / curr))
                if tokens[i] == "*":
                    stack.append(int(prev * curr))
        return int(stack.pop())
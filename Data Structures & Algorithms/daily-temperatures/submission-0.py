class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return [0]
        stack = [0]
        answer = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                        answer[stack[-1]] = i - stack[-1]
                        stack.pop()
                stack.append(i)
        return answer
                


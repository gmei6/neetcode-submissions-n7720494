class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for element in s: 
            if element in closeToOpen:
                if stack and stack[-1] == closeToOpen[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)

        return True if not stack else False
            
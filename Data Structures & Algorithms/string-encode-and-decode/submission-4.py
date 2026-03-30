class Solution:

    def encode(self, strs: List[str]) -> str:
        # Combine all inputted strings into a single string, maybe use some 
        # special character to differentiate the strings
        output = ""

        for string in strs:
            length = len(string)
            output += str(length)
            output += "#"
            output += string
        print(output)
        return output

    
    def decode(self, s: str) -> List[str]:
        # Decode the inputted string into a list of strings. 
        output = []
        i = 0
        n = len(s)

        while i < n:
            # First determine the length of the number before the string
            # For example, we can expect "4#neet5#codes"
            j = i
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i : j])
            output.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        




        return output







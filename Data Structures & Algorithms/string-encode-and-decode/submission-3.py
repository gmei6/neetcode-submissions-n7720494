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

    def decode(self, s: str) -> list[str]:
        output = []
        index = 0
        n = len(s)

        while index < n:
            # 1) Read the length (one or more digits)
            if not s[index].isdigit():
                index += 1
                continue

            j = index
            while j < n and s[j].isdigit():
                j += 1

            # Now s[index:j] is the full length; next char should be '#'
            if j >= n or s[j] != '#':
                # malformed input; handle as you prefer
                break

            length = int(s[index:j])

            # 2) Read the word of that length right after '#'
            start = j + 1
            end = start + length
            output.append(s[start:end])

            # 3) Advance index to after the word
            index = end

        return output


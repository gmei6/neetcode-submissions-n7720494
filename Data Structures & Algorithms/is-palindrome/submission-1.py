import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = s
        copy = copy.replace(" ", "")
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)

        copy = clean
        copy = copy.upper()
        print(copy)

        index = 0

        for character in copy:
            print("This is the character we are comparing", character, copy[len(copy) - index - 1])
            if (character != copy[len(copy) - index - 1]):
                print("We are returning false")
                return False
            index += 1
            print("The values are equal")
            print("")


        return True


        
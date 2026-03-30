class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for element in strs:
            chars = [0] * 26

            for char in element:
                chars[ord(char) - ord('a')] += 1
            map[tuple(chars)].append(element)
        return list(map.values())






























        '''
        output = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            output[tuple(count)].append(s)
        return list(output.values())
        '''
            
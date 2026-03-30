class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.hashmap[key]) - 1
        result = ""

        while l <= r:
            m = (l + r) // 2
            if self.hashmap[key][m][1] < timestamp:
                l = m + 1
                result = self.hashmap[key][m][0]
            elif self.hashmap[key][m][1] > timestamp:
                r = m - 1
            else:
                return self.hashmap[key][m][0]
        return result
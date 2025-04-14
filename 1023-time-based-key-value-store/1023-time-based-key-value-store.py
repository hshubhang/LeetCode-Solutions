from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.timestamp_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_dict:
            self.timestamp_dict[key] = SortedDict()
        self.timestamp_dict[key][timestamp] = value
        
      
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_dict:
            return ""
        
        it = self.timestamp_dict[key].bisect_right(timestamp)

        if it == 0:
            return ""
        return self.timestamp_dict[key].peekitem(it - 1)[1]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
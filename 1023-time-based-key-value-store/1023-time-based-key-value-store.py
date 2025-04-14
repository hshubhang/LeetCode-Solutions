class TimeMap:

    def __init__(self):
        self.timestamp_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp_dict:
            self.timestamp_dict[key] = []
        self.timestamp_dict[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_dict:
            return ""
        arr = self.timestamp_dict[key]
        result = ""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                result = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
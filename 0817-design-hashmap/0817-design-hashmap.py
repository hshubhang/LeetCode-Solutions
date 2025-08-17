class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map_arr = [[] for _ in range(self.size)]


    def put(self, key: int, value: int) -> None:
            idx = key % self.size
            bucket = self.map_arr[idx]
            for i, (k,v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.size
        for k, v in self.map_arr[idx]:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        idx = key % self.size
        bucket = self.map_arr[idx]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
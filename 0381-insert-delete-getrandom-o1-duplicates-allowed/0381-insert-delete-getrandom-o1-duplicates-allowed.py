class RandomizedCollection:

    def __init__(self):
        self.dictionary = {}
        self.arr = []
    def insert(self, val: int) -> bool:

        if val in self.dictionary:
           self.dictionary[val].add(len(self.arr))
           self.arr.append(val)
           return False
        else:
            self.dictionary[val] = {len(self.arr)}
            self.arr.append(val)
            return True
        
    def remove(self, val: int) -> bool:

        if val in self.dictionary:

            index_set = self.dictionary[val]
            index_to_remove = index_set.pop()
            last_element = self.arr[-1]
            last_index = len(self.arr) - 1
            if index_to_remove != last_index:
                
                self.arr[index_to_remove] = last_element
                self.arr[last_index] = val
                self.dictionary[last_element].remove(last_index)
                self.dictionary[last_element].add(index_to_remove)
                self.arr.pop()
                if not self.dictionary[val]:
                    del self.dictionary[val]
                return True
            else:
                self.arr.pop()
                if not self.dictionary[val]:
                    del self.dictionary[val]
                return True
               
                return True
        return False
                # Dict = {1:(0,1), 2: (1)}
                #remove(1)
                #index_to_remove = 1
                #last_element = 2
                #last_index = 2
                #dict[2].add(1)
                #
            


    def getRandom(self) -> int:

        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
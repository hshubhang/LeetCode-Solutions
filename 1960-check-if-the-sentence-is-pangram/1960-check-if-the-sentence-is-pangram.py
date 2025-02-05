class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = defaultdict()
        for i in string.ascii_lowercase:
            hashmap[i] = 0
        for i in sentence:
            if i in hashmap:
                hashmap[i] += 1
        
        if any(value == 0 for value in hashmap.values()):
            return False
        else:
            return True
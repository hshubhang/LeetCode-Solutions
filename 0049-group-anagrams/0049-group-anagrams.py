class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word not in hashmap:
                hashmap[word] = []
            hashmap[word].append(i)
        return list(hashmap.values())



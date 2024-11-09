class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = []
            hashmap[i].append(i)
        sorted_hash = sorted(hashmap, key=lambda k: len(hashmap[k]), reverse=True)
        frequent_most = sorted_hash[:k]
        return frequent_most

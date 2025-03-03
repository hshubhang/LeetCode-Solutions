from typing import List
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        
        for num_list in (nums1, nums2):
            for idx, val in num_list:
                hashmap[idx] += val

        return sorted([[idx, val] for idx, val in hashmap.items()])

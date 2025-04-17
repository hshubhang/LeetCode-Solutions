class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mon_stack = []
        hashmap = {}

        for i in nums2:
            while mon_stack and i > mon_stack[-1]:
                hashmap[mon_stack.pop()] = i             
            mon_stack.append(i)

        while mon_stack:
            hashmap[mon_stack.pop()] = -1

        return [hashmap.get(i, -1) for i in nums1]
 


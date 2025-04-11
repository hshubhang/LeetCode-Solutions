class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        print(nums1_copy)
        ptr1 = 0
        ptr2 = 0
        p = 0
        while ptr1 < m or ptr2 < n:
            if ptr1 < m and (ptr2 >= n or nums1_copy[ptr1] <= nums2[ptr2]):
                nums1[p] = nums1_copy[ptr1]
                ptr1 += 1
            else:
                nums1[p] = nums2[ptr2]
                ptr2 += 1
            p += 1
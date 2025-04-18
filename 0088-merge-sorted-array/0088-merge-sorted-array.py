class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        p = (m + n) - 1

        for p in range(m+n-1, -1, -1):
            if ptr2 < 0:
                break
            elif ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[p] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[p] = nums2[ptr2]
                ptr2 -= 1
            

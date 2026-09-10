class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2,nums1 = nums1,nums2

        left = 0
        right = len(nums1)

        while left <= right:
            i = (left + right)//2
            j = (len(nums1)+len(nums2)+1)//2 - i


            al = nums1[i-1] if i > 0 else float("-inf")
            ar = nums1[i] if i <len(nums1) else float("inf")

            bl = nums2[j-1] if j> 0 else float("-inf")
            br = nums2[j] if j < len(nums2) else float("inf")

            if al <= br and bl <= ar:
                if (len(nums2) + len(nums1))%2 == 1:
                    return max(al,bl)

                else:
                    return (max(al,bl)+min(ar,br)) / 2

            if al > br:
                right = i - 1
            else:
                left = i + 1

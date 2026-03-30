class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Somehow I need to perform a binary search when the two arrays are apart
        # from each other. 
        # Example:
        # [1, 3], [2,4]

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(nums1) > len(nums2):
            A, B = nums2, nums1

        # We now know that A is the smaller array
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - 2 - i 

            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i+1] if (i+1) < len(A) else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j+1] if (j+1) < len(B) else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                # Consider if m + n is odd
                if total % 2 == 1:
                    return min(A_right, B_right)

                # Consider if m + n is even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left >= B_right:
                r = i - 1
            else:
                l = i + 1



class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)

        result = []
        
        indexes = dict()

        for i in range(m):
            indexes[nums2[i]] = i

        for i in range(n):
            nextMax = -1
            for j in range(indexes[nums1[i]],m):
                if( nums2[j] > nums1[i] ):
                    nextMax = nums2[j]
                    break
            result.append(nextMax)

        return result
            
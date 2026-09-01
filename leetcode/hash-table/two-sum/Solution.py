class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash = {}

        n= len(nums) 
        for i in range(n):
            x = nums[i]
            y = target - x
            if( y in hash ):
                return [i,hash[y]]
            hash[x] = i

        return []
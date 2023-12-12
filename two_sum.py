class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)-1): 
            val1  = nums[x]
            for y in range(x+1, len(nums)):
                val2 = nums[y]
                if val1 + val2==target:
                    return [x,y]
        


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        moin = {}
        for i in range(len(nums)):
            
            complement = target-nums[i]

            if complement in moin:
                return [i, moin[complement]]
            
            moin[nums[i]] = i
                



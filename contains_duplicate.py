class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()  

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


    def containsDuplicate(self, nums):
        seen = {}
        for i in nums:
            if i in seen:
                return seen[i]
            seen[i] = True
        return False
from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):            
            temp = nums.pop(i)
            product = reduce((lambda x, y: x * y), nums, 1)

            res.append(product)
            nums.insert(i, temp)

        return res


sol = Solution()

print(sol.productExceptSelf([-1,1,0,-3,3]))
print(sol.productExceptSelf([1,2,3,4]))

# print()
        
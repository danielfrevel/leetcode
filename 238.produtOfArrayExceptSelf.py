from functools import reduce

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        l = 1
        r = 1
        result = [0]*n
        for i in range(n):
            result[i] = l
            l *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= r
            r *= nums[i]
        return result


sol = Solution()

print(sol.productExceptSelf([-1,1,0,-3,3]))
print(sol.productExceptSelf([1,2,3,4]))

# print()
        
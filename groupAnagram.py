class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}

        for i in strs: 
            sortedI = "".join(sorted(i))
            if sortedI not in result:
                result[sortedI] = [i]
            else: 
                result[sortedI].append(i)

        return list(result.values())

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
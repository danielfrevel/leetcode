class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}


        seenAnagrams = set()
        for i in strs: 
            sortedI = [c for c in i]
            sortedI.sort()
            sortedI = "".join(sortedI)
            if sortedI not in seenAnagrams:
                seenAnagrams.add(sortedI)
            if sortedI not in result:
                result[sortedI] = [i]
            else: 
                result[sortedI].append(i)

        return result.values()


sol = Solution()

print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
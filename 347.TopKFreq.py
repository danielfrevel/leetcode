import functools

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()

        # für jedes element checken ob das vorherige gleich ist
        # wenn ja dann counter erhöhen
        # wenn nein dann counter in dict eintragen
        # dict nach value sortieren
        # die k größten values zurückgeben
        
        lastKey = None
        counter = 0
        dict = {}
        for num in nums:
            if num == lastKey:
                counter += 1
            else:
                if lastKey != None:
                    dict[lastKey] = counter
                counter = 1
                lastKey = num

        dict[lastKey] = counter

        sortedDict = sorted(dict.items(), key=lambda x: x[1], reverse=True) # Max Heap

        lastKeys = []
        for i in range(k):
            lastKeys.append(sortedDict[i][0])

         

        return lastKeys         

sol = Solution()

print(sol.topKFrequent([1,1, 2,3,3,3,], 2))